from random import choice


many_word = ["champion", "dungeon", "homework"]
word = choice(many_word)
list_word = list(word)


random_list = []

# print(list_word)
while len(list_word) > 0:
    char = choice(list_word)
    random_list.append(char)
    list_word.remove(char)
# print(list_word)
print(*random_list, sep = ", ")
# flag = False
# while flag == False:
#     user_word = input("Your answer: ")
#     if user_word == word:
#         flag = True
# if flag == True:
#     print("Hura")
# else:
#     print(":(")    

# while True:
#     user_word = input("Your answer: ")
#     if user_word == word:
#         print("Hura")
#         break
#     else:
#         print(":(")