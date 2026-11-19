import sqlite3
import pandas as pd

# read the csv with video sample metadata
videoSample = pd.read_csv("data/videoIDs.csv", dtype=str)

# connect to SQLite
connection = sqlite3.connect("data/tiktokResearch.db")
cursor = connection.cursor()

# inserting manually sampled videos from CSV into SQLite
insert_query = """
    INSERT OR IGNORE INTO videoIDs (
        videoID,
        videoURL,
        sampleID,
        datePosted
    )
    VALUES (?, ?, ?, ?)
"""

# converts each row to a tuple and executes INSERT for every row
cursor.executemany(
    insert_query,
    videoSample.itertuples(index=False, name=None)
)
connection.commit()

# counts number of rows in table and prints
cursor.execute("SELECT COUNT(*) FROM videoIDs")
videoCount = cursor.fetchone()[0]

# prints results
print("VIDEO SAMPLE IMPORT")
print("-------------------")
print("Rows in CSV: ", len(videoSample))
print("Rows in DB: ", videoCount)

# closes connection
connection.close()