from flask import *
from service import service_collection
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("homepage.html")
  
@app.route('/all-service')
def all_service():
  all_service = service_collection.find()
  return render_template('service.html', all_service = all_service)
  

# Cách 1: 

  # tạo ra 2 route /male và /female
  # services = service_collection.find({"gender": "male"})  
  # services = service_collection.find({"gender": "female"})



# Cách 2:

# @app.route('/all-service/<gender>')
# def all_service_gender(gender):
#   all_service = service_collection.find()
#   return render_template('service_gender.html', all_service = all_service, gender_1 = gender)


# Cách 3:
# Không tạo thêm templates

@app.route('/all-service/<gender>')
def all_service_gender(gender):
  all_service = service_collection.find({"gender" : gender})
  return render_template('service.html', all_service = all_service)


@app.route('/all-service/details/<id>')
def details(id):
  detail_service = service_collection.find_one({"_id": ObjectId(id)})
  return render_template("detail_service.html", service = detail_service)


@app.route('/delete/<id>')
def delete(id):
  delete_service = service_collection.find_one({"_id": ObjectId(id)})
  if delete_service is not None:
    service_collection.delete_one(delete_service)
    return redirect('/all-service')
  else:
    return "Not found service"

@app.route('/update/<id>', methods = ["GET", "POST"])
def update(id):
  edit_service = service_collection.find_one({"_id":ObjectId(id)})
  if request.method == "GET":
    return render_template("update_service.html", edit_service = edit_service)
  elif request.method == "POST":
    form = request.form 
    name = form["full_name"]
    age = form["age"]
    address = form["address"]
    gender = form["gender"]
    available = form["available"]
    new_value = {"$set" : {
      "name" : name,
      "age" : age,
      "address" : address,
      "gender" : gender,
      "available" : available,
    }}
    service_collection.update_one(edit_service, new_value)
    return redirect("/all-service/details/{0}".format(id))

@app.route('/login', methods = ["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    form = request.form
    username = form["username"]
    password = form["password"]
    if username == "admin" and password == "admin":
      session["logged"] = True
      return redirect('/all-service')
    else:
      return redirect('/login')

if __name__ == '__main__':
  app.run(debug=True)
 

 # Tìm hiểu thêm về relative path và absolute path

 