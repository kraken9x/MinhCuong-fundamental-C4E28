from model import services
from faker import Faker
from random import randint, choice
faker = Faker()

for i in range(50):
    new_service = {
        "name" : faker.name(),
        "address" : faker.address(),
        "age" : randint(18, 30),
        "gender" : choice(["male", "female"]),
        "height" : randint(150, 190)
    }

    services.insert_one(new_service)
    print("Save document {0}...".format(i+1))