def calc(x, y, para):
    if para == "+":
        total = x + y
    elif para == "-":
        total = x - y
    elif para == "*" or para == "x":
        total = x * y
    elif para == "/" or para == ":":
        total = x / y
    else:
        total = "Error!!"        
    return total

a = calc(5, 7, "-")
print(a)