from flask import *
from database import bike_collection
from random import randint, choice
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello World"

@app.route('/new_bike', methods = ["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("index.html")
    else:
        form = request.form 
        # print(form)
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        new_item = {
            "model" : model,
            "fee" : fee,
            "image" : image,
            "year" : year,
        }
        bike_collection.insert_one(new_item)
        return redirect("/new_bike")
if __name__ == '__main__':
  app.run(debug=True)
 