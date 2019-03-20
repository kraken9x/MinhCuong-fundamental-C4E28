from random import randint

print('''
Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
Press
'c' -> correct
's' -> smaller
'l' -> larger
''')

low = 1
high = 101

while True:

    mid = (low + high)//2 #chia lấy phần nguyên

    # x = 100

    # print("Is {0} your number {1}?".format(mid, x))
    answer_input = input("Is {0} your number? ".format(mid))

    if answer_input == 'c':
        print("I knew it")
        break
    elif answer_input == 'l':
        high = mid
    elif answer_input == 's':
        low = mid



