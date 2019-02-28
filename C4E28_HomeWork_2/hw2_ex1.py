#Exercise 1:

height = int(input("Please enter your height in cm? "))
weight = int(input("please enter your weight in kg? "))
height = height*0.01
bmi = weight/(height*height)
sen = ""
if bmi > 0 and bmi < 16:
    sen += "severely underweight"
elif bmi >= 16 and bmi < 18.5:
    sen += "underweight"
elif bmi >= 18.5 and bmi < 25:
    sen += "normal"
elif bmi >= 25 and bmi < 30:
    sen += "overweight"
elif bmi >= 30:
    sen += "obese"
else:
    sen = ""    
print("your BMI index is", bmi, "and you are", sen)
