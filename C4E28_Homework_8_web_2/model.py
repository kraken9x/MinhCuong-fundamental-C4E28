import mongodb

database = mongodb.connect()

posts = database["posts"]

