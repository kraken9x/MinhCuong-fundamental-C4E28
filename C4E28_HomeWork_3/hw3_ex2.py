sheep = [5, 7, 300, 90, 24, 50, 75]
print("\n1. Hello, My name is Cường and these are my sheep sizes")
print(sheep)

print("\n2. Hello, My name is Cường and these are my sheep sizes")
print(sheep)
print("Now my biggest sheep has size {} and let's shear it".format(max(sheep)))

print("\n3. Hello, My name is Cường and these are my sheep sizes")
print(sheep)
print("Now my biggest sheep has size {} and let's shear it".format(max(sheep)))
max_size = max(sheep)
for index, item in enumerate(sheep):
    if item == 300:
        sheep[index] = 8
print(sheep)

print("\n4. Hello, My name is Cường and these are my sheep sizes")
print(sheep)
print("Now my biggest sheep has size {} and let's shear it".format(max(sheep)))
max_size = max(sheep)
for index, item in enumerate(sheep):
    if item == max_size:
        sheep[index] = 8
print(sheep)
print("One month has passed, now here is my flock")
for index, item in enumerate(sheep):
    sheep[index] += 50
print(sheep)

print("\n5. Hello, My name is Cường and these are my sheep sizes")
print(sheep)
print("Now my biggest sheep has size {} and let's shear it".format(max(sheep)))
max_size = max(sheep)
for index, item in enumerate(sheep):
    if item == max_size:
        sheep[index] = 8
print(sheep)
month = 1
while True:    
    print("{} month has passed, now here is my flock".format(month))   
    for index, item in enumerate(sheep): 
        sheep[index] += 50*month
    month += 1
    print(sheep)
    if month == 4:
        break

print("\n6. My flock has size in total: ", end = "")
sum = 0
for i in range(0,len(sheep)):
    sum += sheep[i]
print(sum)
print("I would get ", sum, " * 2$ = ", sum*2, "$")
