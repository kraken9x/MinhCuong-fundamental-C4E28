#Exercise 1:

menu = ["T-Shirt", "Sweater"]

loop = True
while loop:
    inp = str(input("Welcome to our shop, what do you want (C, R, U, D)? ")).upper()
    if(inp == "C"):
        add = input("Enter new item: ")
        menu.append(add)
        print("Our items:", end = " ")
        print(*menu, sep = ", ")
    elif(inp == "R"):
        print("Our items:", end = " ")
        print(*menu, sep = ", ")    
    elif(inp == "U"):
        posi = int(input("Update position? "))
        edit = input("New item? ")
        menu[posi-1] = edit
        print("Our items:", end = " ")
        print(*menu, sep = ", ")
    elif(inp == "D"):
        dele = int(input("Delete position? "))
        del menu[dele-1]
        print("Our items:", end = " ")
        print(*menu, sep = ", ")
    else:
        loop = False
        print("Bye bye!")


