from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/user/<username>')
def display_user(username):

    users = {
        "huy" : {
            "name" : "Nguyen Quang Huy",
            "age" : 29,
            "gender" : "male",
            "hobbies" : "reading books, coding"
        },
        "tuananh" : {
            "name" : "Huynh Tuan Anh",
            "age" : 22,
            "gender" : "male",
            "hobbies" : "singing, hanging out"
        }
    }
    for key, value in users.items():
        if username == key:
            page = "index.html"
            break
        else:
            page = "notfound.html"

    return render_template(page, users = users, username = username)

if __name__ == '__main__':
    app.run(debug=True)