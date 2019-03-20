
fav = ["death note", "netflix", "teaching"]

print("Hi there, here are my favourite so far")
print(*fav, sep = ", ")
thing = input("Name one thing you want to add? ")
fav.append(thing)
print(*fav, sep = ", ")

