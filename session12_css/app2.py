#fapp to automatic take flask form
from flask import *
from services import services_collection
from bson.objectid import ObjectId
app = Flask(__name__)

app.config["SECRET_KEY"]= "hgfjhgfjhfjhgvnbfvbkg"

mongo_uri = "mongodb+srv://admin:admin@c4e28-xzlj8.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
services_database = client.db_services
bike = services_database["bike"]

@app.route('/')
def index():
    session["logged"] = False
    return render_template('homepage.html')

@app.route('/all_services')
def all_services():
    if session["logged"] == True:
        all_services = services_collection.find()
        return render_template("all_services.html", all_services = all_services)
    else: 
        return redirect('/login')


@app.route('/all_services/<gender>')
def services(gender):
    all_services = services_collection.find({"gender": gender})
    return render_template("all_services.html", all_services = all_services)
    
@app.route('/all_services/detail/<id>')
def detail(id):
    detail_service = services_collection.find_one({"_id": ObjectId(id)})
    return render_template("detail.html", detail_service = detail_service)

@app.route('/delete/<id>')
def detele(id):
    del_service = services_collection.find_one({"_id": ObjectId(id)})
    if del_service != None:
        services_collection.delete_one(del_service)
    else:
        print ("Not found")
    return redirect('/all_services')

@app.route('/update/<id>', methods=["GET", "POST"])
def update(id):
    edit_service = services_collection.find_one({"_id": ObjectId(id)})
    if request.method == "GET":
        return render_template("update.html", edit_service = edit_service)
    elif request.method == "POST":
        form = request.form
        name = form["full_name"]
        age = form["age"]
        address = form["address"]
        gender = form["gender"]
        new_value = {"$set": {
            "name": name,
            "age": age,
            "address": address,
            "gender": gender,
        }}
        services_collection.update_one(edit_service, new_value)
        return redirect('/all_services/detail/{0}'.format(id))

@app.route('/login', methods= ["GET", "POST"])
def login():
    if session["logged"] == True:
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            form = request.form
            username = form["username"]
            password = form["password"]
            if username == "admin" and password == "adminc4e":
                session["logged"] = True
                return "Logged in"
            else:
                return "Not found"
    else:
        return redirect('/all_services')


@app.route('/logout')
def logout():
    # del session["logged"] # Cach 1
    session["logged"] = False # Cach 2
    return redirect('/login')


@app.route('/new_bike', methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        new_value = {
            "model": model,
            "fee": fee,
            "image": image,
            "year": year,
        }
        bike.insert_one(new_value)
        return redirect('/new_bike')

if __name__ == '__main__':
    app.run(debug=True)