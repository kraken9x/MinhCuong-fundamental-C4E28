prices = {}

prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

# for key, value in prices.items():
#     print(key, value)

stock = {}

stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15


# for key, value in prices.items():
#     print(key, value)

for key, value in prices.items():
    print(key)
    print("price:", prices[key])
    print("stock:", stock[key])

total = 0
for key, value in prices.items():
    total += value + stock[key]
print("total =", total)