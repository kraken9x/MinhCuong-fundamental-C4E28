from random import randint

number = randint(1, 100)
print(number)
#Cách 1:
count = 0
playing = True
# while playing:
#     if count < 3:
#         guess = int(input("Guess my number (1-100)? "))   
    
#         if number > guess:
#             print("Too small !!")
#         elif number < guess:
#             print("Too large !!")
#         else:
#             print("Bingo")
#             playing = False
#     else:
#         break
#     count += 1

#Cách 2:
while playing:
    guess = int(input("Guess my number (1-100)? "))   

    if number > guess:
        print("Too small !!")
    elif number < guess:
        print("Too large !!")
    else:
        print("Bingo")
        break
    count += 1
    if count == 7:
        print("You loose")
        playing = False
