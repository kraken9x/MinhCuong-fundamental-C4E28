# r1 = range(10)
# print(*r1)


# print(r1) #=> range(0, 10)
# print(*r1) #=> 0 1 2 3....10
# r2 = range(5, 10)
# print(*r2) #=> 5 6...10

# r3 = range(5, 20, 3) #=> 5 8 11 ... 17
# #range(start, stop, step)


# # in ra các số chẵn 3->100
# r1 = range(4, 100, 2)
# print(*r1)

# #in các số từ 100 -> 5
# r2 = range(100, 5, -1)
# print(*r2)

# #in các số từ 1000->100 chia hết cho 5
# r3 = range(1000, 99, -5)
# print(*r3)

#for i in range(4): tương đương với for in in [0, 1, 2, 3]:
# for i in [0, 1, 2, 7]:
#     print("hi")

# sum = 0
# for i in range(11):
#     sum = sum + i
# print(sum)



# sum1 = 0
# for i in range(11):
#     sum1 = sum1 + i*i
# print(sum1)

#cách 2: sử dụng hàm sum([1, 2, 3...])

print(*range(1,11))

