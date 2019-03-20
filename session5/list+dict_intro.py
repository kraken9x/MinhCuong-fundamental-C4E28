# people = [
#     {
#         "name"  : "Quan",
#         "salary": 25,
#         "hour"  : 3,
#         "day"   : 20
#     },
#     {
#         "name"  : "Duc",
#         "salary": 80,
#         "hour"  : 5,
#         "day"   : 15
#     }
# ]


# print(people[0]["name"])


# name = input("Enter name: ")

# for index, item in enumerate(people):
#     salary_total = item["salary"]*item["hour"]*item["day"]
#     if item["name"] == name:
#         print(salary_total)
#         break
#     else:
#         print("Not found")
#         break



#CÁCH 2

# for index, item in enumerate(people):
#     found = False
#     salary_total = item["salary"]*item["hour"]*item["day"]
#     if item["name"] == name:
#         found = True
#     else:
#         found = False
# if found:
#     print(salary_total)
# else:
#     print("Not found")

#=> TÁCH RA LÀM 3 PHẦN RÕ RÀNG, INPUT, LOGIC (có thể tái sử dụng), và IN RA MÀN HÌNH (OUTPUT)

# total = 0
# for index, item in enumerate(people):
#     salary_total = item["salary"]*item["hour"]*item["day"]
#     total = total + salary_total
    
# print("The total salary of these two people is ", end = "")
# print(total)



# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# print(x + y)


#SCOPE: biến sinh ra ở đâu thì sẽ chết ở đó




# app.py -> No module name Pyqt5

# pip install Pyqt5
# lên trang pypi
# code logic o freakingmath.py
# chay o app.py

# tao 2 ham o freakingmath.py

# check_answer() => đúng thì dùng return True
# sai thì dùng return false




loop = True
while loop:
    x   = int(input("Enter x: "))
    y   = int(input("Enter y: "))
    op  = input("Enter operator: ")
    total = 0

    if op == "+":
        total += x + y
    elif op == "-":
        total += x - y
    elif op == "*" or op == "x":
        total += x * y
    elif op == "/" or op == ":":
        total += x / y
    else:
        total = "Error!!"
        loop = False

    print(total)