from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@pilot-app-q5prm.mongodb.net/test?retryWrites=true"

# 1. Connect to data base via link above (copy link from mongodb.com)

client = MongoClient(mongo_uri)

# 2. Get database
db = client.test

# 3. Create collection
games = db["games"]

# 4. Create document
new_game = {
    "name" : "Pikachu",
    "description" : "Always lost money",

}
# 5. Insert document

games.insert_one(new_game)