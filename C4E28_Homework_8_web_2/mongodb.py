from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect to data base via link above (copy link from mongodb.com)

client = MongoClient(mongo_uri)

# 2. Get database

def connect():
    db = client.c4e
    return db
