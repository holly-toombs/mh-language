import sqlite3

# connects to SQLite
connection = sqlite3.connect("data/tiktokResearch.db")
print("Database connection successful")

# lets python execute SQL statements
cursor = connection.cursor()

# creates the videoIDs table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS videoIDs (
        videoID TEXT PRIMARY KEY,
        videoURL TEXT,
        sampleID TEXT,
        datePosted TEXT
    )""")

# cursor.execute("DROP TABLE IF EXISTS videosMD")

# creates the videosMD table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS videosMD (
        videoID TEXT PRIMARY KEY,
        username TEXT,
        vidDesc TEXT,
        dateCreated INTEGER,
        region TEXT,
        viewCount INTEGER,
        likeCount INTEGER,
        commentCount INTEGER,
        shareCount INTEGER,
        favesCount INTEGER,
        hashtags TEXT,
        duration INTEGER,
        retrievedAT TEXT,
        transcript TEXT,
        videoTag TEXT,
        videoLabel TEXT,
        hashtagInfo TEXT,
        isStemVerified INTEGER
    )
""")

# creates the creatorsMD table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS creatorsMD (
        username TEXT PRIMARY KEY,
        videoCount INTEGER,
        followerCount INTEGER,
        likesCount INTEGER,
        inclVideos INTEGER DEFAULT 0,
        isVerified INTEGER,
        displayName TEXT,
        bioDescription TEXT,
        retrievedAt TEXT
        )
""")

# creates the queryLog table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS queryLog (
        requestID INTEGER PRIMARY KEY AUTOINCREMENT,
        startDate TEXT,
        endDate TEXT,
        videoIDsQueried TEXT,
        requestTime TEXT,
        httpStatus INTEGER,
        apiErrorCode TEXT,
        logID TEXT,
        resultCount INTEGER,
        outcome TEXT,
        cursor INTEGER,
        searchID TEXT,
        hasMore INTEGER
    )
""")

# commits changes
connection.commit()

# verifies that table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Database tables:", tables)

# alternative to hide internal tables
# cursor.execute("""
#     SELECT name
#     FROM sqlite_master
#     WHERE type = 'table'
#     AND name NOT LIKE 'sqlite_%'
# """)

# closes the SQLite connection
connection.close()
print("Database connection closed")