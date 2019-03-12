def get_even_list(l):
    new_arr = []
    for index, item in enumerate(l):
        if item%2 == 0:
            new_arr.append(item)

    return new_arr

print(get_even_list([1,-2,3,4,5,-6,7,8]))