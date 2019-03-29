from pymongo import MongoClient
from faker import Faker
from random import randint, choice
from bson.objectid import ObjectId
faker = Faker()

mongo_uri = "mongodb+srv://admin:admin@pilot-app-chof7.mongodb.net/test?retryWrites=true"

# 1. Connect to cluster

client = MongoClient(mongo_uri)

# 2. Get / Create database

service_database = client.db_service # đằng sau dấu chấm là tên database để đặt. Nếu đã tồn tại db thì sẽ get về lưu vào biến, nếu chưa thì sẽ tạo mới.

# 3. Get / Create collection

service_collection = service_database["service"]

# 4. Create document, insert document

# for i in range(50):
#     new_service = {
#         "name" : faker.name(),
#         "age" : randint(18, 30),
#         "address" : faker.address(),
#         "gender" : choice(["male", "female"]),
#         "available" : choice([True, False])

#     }
#     service_collection.insert_one(new_service)
#     print("insert service number {0} .....".format(i+1))

# 5. Read data
# 5.1 Read All 

all_services = service_collection.find() # cơ chế lazy loading

# Trả về kiểu dữ liệu cursor, gần giống list
# print(all_services)
# for service in all_services:
#     print(service["name"])

# TRẢ VỀ 1 LIST
# Điều kiện trong find() giống trong find_one() => trả về 1 list gồm các phần tử giống nhau



# 5.2 Read one 
# # Chỉ trả về duy nhất 1 document
# one_service = service_collection.find_one({"name" : "Kimberly Graham"})
# Trả về document lần lượt từ trên xuống dưới

# read = query 

# dữ liệu bson gần giống json. khác là có thêm ngày tháng

# one_service_2 = service_collection.find_one({"_id" : ObjectId('5c9a1dccd3ed8b3fcc2bf91b')})

# print(one_service_2)




# 6. DELETE

service = service_collection.find_one({"_id" : ObjectId("5c9a1dc7d3ed8b3fcc2bf8f5")})
if service != None:
    service_collection.delete_one(service)
else:
    print("Not Found")
# print(service) # sau khi xóa thì console hiện none
