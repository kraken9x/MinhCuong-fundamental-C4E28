from pymongo import MongoClients

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect to data base via link above (copy link from mongodb.com)

client = MongoClient(mongo_uri)

# 2. Get / Create database

database = client.get_database() 
# 3. Get / Create collection

rivers = database["river"]

rivers_africa = rivers.find({"continent":"Africa"})

# for river in rivers_africa:
#     print(river["name"])
#     print("----------")


rivers_s_america = rivers.find({"continent":"S. America"})

for river in rivers_s_america:
    if river["length"] < 1000:
        print(river["name"])
        print("----------")