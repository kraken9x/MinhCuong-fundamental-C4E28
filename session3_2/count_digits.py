# while True:
#     numb = int(input("Enter your number? "))

#     counting = True
#     count = 0
#     while counting:
#         numb = numb // 10
#         count += 1
#         if numb == 0:
#             counting = False

#     print("Số chữ số của số nhập vào là:", count)


while True:
    numb = int(input("Enter your number? "))

    count = 0
    while numb != 0:
        numb = numb // 10
        count += 1

    print("Số chữ số của số nhập vào là:", count)