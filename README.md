# Extended Research Project - Holly/Nina

Python scripts for video sampling using the TikTok Research API.

## Workflow
1. Import manually sampled video IDs into SQLite.
2. Retrieve video metadata using the API.
3. Track queries and identify unique creators.
4. Retrieve creator metadata.
5. Export datasets for analysis.

## Files
- `setupDB.py`: Creates database tables
- `importVideos.py`: Imports sampled videos
- `videosRT.py`: Retrieves video metadata
- `creatorsRT.py`: Retrieves creator metadata
- `exportData.py`: Exports datasets

## Status
- Database setup complete & works on pilot sample
- API retrieval script in progress
- Next need to test on pilot sample