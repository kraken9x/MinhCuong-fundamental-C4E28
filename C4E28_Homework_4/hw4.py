quiz = [
    {
        "question"  : "If x = 8, then what is the value of 4(x+3) ?",
        "choices"    : [35, 36, 40, 44]
    },
    {
        "question"  : "Estimate this answer (exact calculation not needed):\nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is Jack's avarage mark?",
        "choices"    : [55, 65, 75, 85]
    }
]
answer = [44, 65]
right  = 0
for index, element in enumerate(quiz):
    for key, value in element.items():
        #print(key)
        if key == "question":
            print(value)
        else:
            for index2, element2 in enumerate(value):
                print("{}. {}".format(index2 + 1, element2)) 
    user_answer = int(input("Your choice? "))
    for key2, value2 in element.items():
        if key2 == "choices":
            if value2[user_answer-1] == answer[index]:
                print("Bingo")
                right += 1
                break
            else:
                print(":(")
                break
if right == 0:
    print("You're a dumb ass")
else:
    print("You correctly answer {} out of 2 questions".format(right))