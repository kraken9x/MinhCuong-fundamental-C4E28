from random import randint, choice
#from calc import calc
import calc
print("*******************")

num_1 = randint(0, 10)
num_2 = randint(0, 10)
op = choice(["+", "-", "*", "/"])
error = randint(-1, 1)
real_result = 0
# if op == "+":
#     real_result += num_1 + num_2
# elif op == "-":
#     real_result += num_1 - num_2
# elif op == "*" or op == "x":
#     real_result += num_1 * num_2
# elif op == "/" or op == ":":
#     real_result += num_1 / num_2
# else:
#     real_result = "Error!!"

# real_result = calc(num_1, num_2, op)
real_result = calc.calc(num_1, num_2, op)

    
print("{0} {2} {1} = ".format(num_1, num_2, op), end = "")
print(real_result + error)
choice = input("Y/N: ")
choice = choice.lower()
sentence = ""
if choice == "y":
    if real_result == real_result + error:
        sentence = "Yay"
    else:
        sentence = "You're wrong"
elif choice == "n":
    if real_result != real_result + error:
        sentence = "Yay"
    else:
        sentence = "You're wrong"
else:
    sentence = "Error"
print(sentence)
print("*******************")


#quy tắc đặt tên biến



# op = input("Enter operator: ")
    

# if op == "+":
#     print("*******************")

#     num_1 = randint(0, 10)
#     num_2 = randint(0, 10)


#     result = num_1 + num_2
#     error = randint(-1, 1)

#     print("{} + {} = ".format(num_1, num_2), end = "")
#     print(result + error)
#     choice = input("Y/N: ")
#     choice = choice.lower()
#     sentence = ""
#     if choice == "y":
#         if result == result + error:
#             sentence = "Yay"
#         else:
#             sentence = "You're wrong"
#     elif choice == "n":
#         if result != result + error:
#             sentence = "Yay"
#         else:
#             sentence = "You're wrong"
#     else:
#         sentence = "Error"
#     print(sentence)
#     print("*******************")

# elif op == "-":
#     print("*******************")

#     num_1 = randint(0, 10)
#     num_2 = randint(0, 10)


#     result = num_1 - num_2
#     error = randint(-1, 1)

#     print("{} - {} = ".format(num_1, num_2), end = "")
#     print(result - error)
#     choice = input("Y/N: ")
#     choice = choice.lower()
#     sentence = ""
#     if choice == "y":
#         if result == result - error:
#             sentence = "Yay"
#         else:
#             sentence = "You're wrong"
#     elif choice == "n":
#         if result != result - error:
#             sentence = "Yay"
#         else:
#             sentence = "You're wrong"
#     else:
#         sentence = "Error"
#     print(sentence)
#     print("*******************")

# elif op == "*" or op == "x":
#     print("*******************")

#     num_1 = randint(0, 10)
#     num_2 = randint(0, 10)


#     result = num_1 * num_2
#     error = randint(-1, 1)

#     print("{} * {} = ".format(num_1, num_2), end = "")
#     print(result * error)
#     choice = input("Y/N: ")
#     choice = choice.lower()
#     sentence = ""
#     if choice == "y":
#         if result == result * error:
#             sentence = "Yay"
#         else:
#             sentence = "You're wrong"
#     elif choice == "n":
#         if result != result * error:
#             sentence = "Yay"
#         else:
#             sentence = "You're wrong"
#     else:
#         sentence = "Error"
#     print(sentence)
#     print("*******************")

# elif op == "/" or op == ":":
#     print("*******************")

#     num_1 = randint(0, 10)
#     num_2 = randint(0, 10)


#     result = num_1 / num_2
#     error = randint(-1, 1)

#     print("{} / {} = ".format(num_1, num_2), end = "")
#     print(result / error)
#     choice = input("Y/N: ")
#     choice = choice.lower()
#     sentence = ""
#     if choice == "y":
#         if result == result / error:
#             sentence = "Yay"
#         else:
#             sentence = "You're wrong"
#     elif choice == "n":
#         if result != result / error:
#             sentence = "Yay"
#         else:
#             sentence = "You're wrong"
#     else:
#         sentence = "Error"
#     print(sentence)
#     print("*******************")

# else:
#     sentence = "Error!!"



