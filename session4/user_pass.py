username = 'c4e'
password = 'codethechange'

user_input = input("Username: ")

# if user_input == username:
#     loop = True
#     i = 0
#     while loop and i <3:
#         password_input = input("Password: ")
#         if password_input == password:
#             print("Welcome")
#             break
#         else:
#             print("wrong password")
#         i += 1
# else:
#     print("User not found")        
count = 0
while True:
    if user_input == username:
        password_input = input("Password: ")
        if password_input == password:
            print("Welcome")
            break
        else:
            print("Wrong password")
            count += 1
            if count == 3:
                print("Login failed!")
                break
    else:
        print("User not found")
        break