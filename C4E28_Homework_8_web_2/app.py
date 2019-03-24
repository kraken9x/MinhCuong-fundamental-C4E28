from model import posts
from faker import Faker
from random import randint, choice
faker = Faker()

new_post = {
    "title" : "C4E28",
    "author" : "Minh Cường",
    "content" : "C4E28 hell yeahhhhhh !!!"
}
posts.insert_one(new_post)
