choices = [35, 36, 40, 44]
answer = choices[3]
print('''
Answer the following algebra question: 
If x = 8, then what is the value of 4(x + 3) ? 
''')
for index, item in enumerate(choices):
    print("{}. {}".format(index+1, item))

count = 0
while True:    
    user_answer = int(input("Your choice: "))
    if choices[user_answer-1] != answer:
        print(":(")
    else:
        print("Bingo")
        break 
    count += 1
    if count == 3:
        print("You're a dumb ass!")
        break