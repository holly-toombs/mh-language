import os
import time
from datetime import datetime, timezone
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

# Settings
BATCH_SIZE = 10
START_DATE = "20260101"
END_DATE = "20260130"

FIELDS = [
    "id", "username", "video_description",
    "create_time", "region_code", "view_count",
    "like_count", "comment_count", "share_count",
    "favorites_count", "hashtag_names", "video_duration"
]

df_test = pd.read_csv("video_ids.csv", dtype=str)

print("Columns found:", df_test.columns.tolist())
print("Number of rows:", len(df_test))
print(df_test.head())

ids = (
    df_test["video_id"]
    .dropna()
    .str.strip()
    .drop_duplicates()
    .tolist()
)

# Authenticate
auth = requests.post(
    "https://open.tiktokapis.com/v2/oauth/token/",
    data={
        "client_key": os.getenv("TIKTOK_CLIENT_KEY"),
        "client_secret": os.getenv("TIKTOK_CLIENT_SECRET"),
        "grant_type": "client_credentials"
    },
    timeout=30
)
auth.raise_for_status()
token = auth.json()["access_token"]

url = "https://open.tiktokapis.com/v2/research/video/query/"
headers = {"Authorization": f"Bearer {token}"}
results = []

# Process batches
for i in range(0, len(ids), BATCH_SIZE):
    batch = ids[i:i + BATCH_SIZE]

    payload = {
        "query": {
            "and": [{
                "operation": "IN",
                "field_name": "video_id",
                "field_values": batch
            }]
        },
        "start_date": START_DATE,
        "end_date": END_DATE,
        "max_count": 100
    }

    while True:
        for attempt in range(3):
            try:
                response = requests.post(
                    url,
                    headers=headers,
                    params={"fields": ",".join(FIELDS)},
                    json=payload,
                    timeout=60
                )
                response.raise_for_status()
                data = response.json()

                if data.get("error", {}).get("code") != "ok":
                    raise RuntimeError(data.get("error"))

                break
            except (requests.RequestException, RuntimeError):
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)

        page = data.get("data", {})
        results.extend(page.get("videos", []))

        if not page.get("has_more"):
            break

        payload["cursor"] = page["cursor"]
        payload["search_id"] = page["search_id"]

    print(f"Processed {min(i + BATCH_SIZE, len(ids))}/{len(ids)} IDs")
    time.sleep(1)

# Match returned metadata to original sample
df = pd.DataFrame(results)
if "id" not in df.columns:
    df["id"] = pd.Series(dtype=str)

df["id"] = df["id"].astype(str)
df = df.drop_duplicates(subset="id")

sample = pd.DataFrame({"video_id": ids})
merged = sample.merge(
    df, left_on="video_id", right_on="id", how="left"
)

merged["matched"] = merged["id"].notna()
merged["retrieved_at_utc"] = datetime.now(
    timezone.utc
).isoformat()

merged.to_csv("tiktok_metadata.csv", index=False)

print(f"Matched {merged['matched'].sum()} of {len(ids)} videos")
print("Saved tiktok_metadata.csv")
