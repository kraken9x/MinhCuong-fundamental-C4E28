from pymongo import MongoClient
mongo_uri = "mongodb+srv://admin:admin@pilot-app-q5prm.mongodb.net/test?retryWrites=true"

# 1. Connect to data base via link above (copy link from mongodb.com)

client = MongoClient(mongo_uri)

# 2. Get database

def connect():
    db = client.test
    return db
