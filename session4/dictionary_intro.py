# # person = ["Duc", 22, "FTU"]


# #dictionary

# #key -> value

# person = {
#     "name": "Duc",
#     "age": 22,
#     "ex-gf": 3,
#     "language": "chinese"
# }

# name = person["name"]
# age = person["age"]
# # print(name)

# # for key in person.keys():
# #     print(key)
# # for value in person.values():
# #     print(value)

# # for key, value in person.items():
# #     print(key, value)


# # CREATE & UPDATE

# #create
# #add vao cuoi cung
# person["city"] = "Hai Phong"

# #update

# person["ex-gf"] = 10

# # DELETE 
# print(person)
# del person["age"]

# print(person)

dictionary = {
    'cc': 'cuc cung',
    'hc': 'hoc',
    'ane': 'anh nho em'
}


teen_code = {
    'cc': 'cuc cung',
    'hc': 'hoc',
    'ane': 'anh nho em'
}

# for i in dictionary.keys():
#     print(i, end = " ")
# print()
# n = input("Your code? ")

# for key, value in dictionary.items():
#     if n == key:
#         print(value)
#         break
#     else:
#         print("Not found")
        
#             m = input("Do you want to contribute this word (Y/N)")
        
#             if m == "N" or m == 'n':
#                 break
#             elif m == "Y" or m == 'y':
#                 x = input("Enter translation: ")
#                 dictionary[n] = x
#                 break
#             else:
#                 print("Please enter (Y/N)")


while True:

    print(*teen_code.keys(), sep = ' ')



    word = input("your code? ")
    if word in teen_code.keys():
        #teen_code.keys() => trả về 1 list gồm các key
        print(teen_code[word])
    else:
        answer = input("Add new word? (Y/N)").lower()
        if answer == 'n':
            print("GoodBye")
            break
        elif answer == 'y':
            new_translation = input("Enter: ")
            teen_code[word] = new_translation


