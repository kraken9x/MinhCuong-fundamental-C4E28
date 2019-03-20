from flask import Flask, render_template, redirect
app = Flask(__name__)

# Without render_template

@app.route('/bmi-1/<int:weight>kg/<int:height>cm')
def caculate_bmi(weight, height):
    sentence = "You are "
    height = height * 0.01
    bmi = weight/(height*height)

    if bmi > 0 and bmi < 16:
        sentence += "severely underweight"
    elif bmi >= 16 and bmi < 18.5:
        sentence += "underweight"
    elif bmi >= 18.5 and bmi < 25:
        sentence += "normal"
    elif bmi >= 25 and bmi < 30:
        sentence += "overweight"
    elif bmi >= 30:
        sentence += "obese"
    else: 
        sentence += "not human, fuck off!"
    return sentence

# With render_template

@app.route('/bmi-2/<int:weight>kg/<int:height>cm')
def caculate_bmi_2(weight, height):
    sentence = "You are "
    height = height * 0.01
    bmi = weight//(height*height)

    if bmi > 0 and bmi < 16:
        sentence += "severely underweight"
    elif bmi >= 16 and bmi < 18.5:
        sentence += "underweight"
    elif bmi >= 18.5 and bmi < 25:
        sentence += "normal"
    elif bmi >= 25 and bmi < 30:
        sentence += "overweight"
    elif bmi >= 30:
        sentence += "obese"
    else: 
        sentence += "not human, fuck off!"

    return render_template("bmi.html", bmi = bmi, sentence = sentence)

if __name__ == '__main__':
    app.run(debug=True)