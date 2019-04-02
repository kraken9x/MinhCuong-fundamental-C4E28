from pymongo import MongoClient
from faker import Faker
from random import randint, choice
from bson.objectid import ObjectId
faker = Faker()

mongo_uri = "mongodb+srv://admin:admin@pilot-app-chof7.mongodb.net/test?retryWrites=true"

# 1. Connect to cluster

client = MongoClient(mongo_uri)

# 2. Get / Create database

bike_database = client.db_bike # đằng sau dấu chấm là tên database để đặt. Nếu đã tồn tại db thì sẽ get về lưu vào biến, nếu chưa thì sẽ tạo mới.

# 3. Get / Create collection

bike_collection = bike_database["bike"]
