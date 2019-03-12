from random import *

def calc(x, y, para):
    if para == "+":
        total = x + y
    elif para == "-":
        total = x - y
    elif para == "*":
        total = x * y
    elif para == "/":
        total = x / y
    else:
        total = "Error!!"        
    return total


def generate_quiz():
    # Hint: Return [x, y, op, result]
    
    x   = randint(1, 10)
    y   = randint(1, 10)
    op  = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    real_result = calc(x, y, op)
    display_result = real_result + error

    return [x, y, op, display_result]

def check_answer(x, y, op, result, user_choice):
    arr = generate_quiz()
    x = arr[0]
    y = arr[1]
    op = arr[2]    
    result = arr[3]
    real_result = calc(x, y, op)
    if user_choice == True:
        if real_result == result:
            return True
        else:
            return False
    else:
        if real_result != result:
            return True
        else:
            return False

