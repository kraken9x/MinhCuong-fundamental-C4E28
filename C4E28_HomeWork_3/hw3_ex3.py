from random import choice


many_word = ["champion", "dungeon", "homework"]


while True:
    word = choice(many_word)
    list_word = list(word)
    random_list = []
    while len(list_word) > 0:
        char = choice(list_word)
        random_list.append(char)
        list_word.remove(char)
    print(*random_list, sep = ", ")

    user_word = input("Your answer: ")
    if user_word == word:
        print("Hura")
        break
    else:
        print(":(")