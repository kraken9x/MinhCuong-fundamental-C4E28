
fav = ["death note", "netflix", "teaching"]

print("Hi there, here are my favourite so far")
for index, item in enumerate(fav):
    print("{0}. {1}".format(index+1, item))
pos = int(input("Position you want to update? "))
pos = pos - 1
element = input("Element you want to update? ")

fav[pos] = element

for index, item in enumerate(fav):
    print("{0}. {1}".format(index+1, item))


# print(*fav, sep = ", ")
# thing = input("Name one thing you want to add? ")
# fav.append(thing)
# print(*fav, sep = ", ")