from flask import Flask, render_template, redirect
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
  return str(detail_service)


@app.route('/delete/<id>')
def delete(id):
  delete_service = service_collection.find_one({"_id": ObjectId(id)})
  if delete_service is not None:
    service_collection.delete_one(delete_service)
    return redirect('/all-service')
  else:
    return "Not found service"

if __name__ == '__main__':
  app.run(debug=True)
 