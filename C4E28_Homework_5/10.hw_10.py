def get_even_list(l):
    new_arr = []
    for index, item in enumerate(l):
        if item%2 == 0:
            new_arr.append(item)

    return new_arr
    
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
