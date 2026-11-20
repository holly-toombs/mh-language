# Extended Research Project - Holly/Nina

Python scripts for video sampling using the TikTok Research API.

## Workflow
1. Manually insert video ID, date, and URL into spreadsheet
2. Import manually sampled video IDs into database (SQLite)
3. Query the API for video metadata
4. Log queries as a paper trail
5. Identify unique creators and insert usernames into separate database
5. Query the API for creator metadata (follower count, age of account, demographics)
6. Export datasets for analysis

## Files
- `setupDB.py`: Creates database tables (videoIDs, videosMD, creatorsMD, queryLog)
    - videoIDs: Copy of manually inputted data from initial spreadsheet
    - videosMD: Retrieved metadata of the 500 sampled videos
    - creatorsMD: Retrieved metadata of all unique influencers
    - queryLog: Log of all API queries made 
- `importVideos.py`: Script to import sampled videos
- `videosRT.py`: Script to retrieve video metadata
- `creatorsRT.py`: Script to retrieve creator metadata (not written yet)
- `exportData.py`: Exports datasets (not written yet)

## Status
- Database setup complete & works on pilot sample
- API retrieval complete & works on pilot sample
- Next:
    - Write script to retrieve creator metadata
    - Test on pilot sample
    - Write script to export databases to .xlsx files for analysis
- Further considerations:
    - How to handle video transcripts - own database needed? How to clean them?
    - Naming conventions for downloaded videos and transcripts, for consistency of indexing