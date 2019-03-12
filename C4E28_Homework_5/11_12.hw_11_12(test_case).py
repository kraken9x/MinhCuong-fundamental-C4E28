def is_inside(list_1, list_2):
    check_length = True
    if len(list_1) ==  2 and len(list_2) == 4:
        x       = list_1[0]
        y       = list_1[1]
        x_rec   = list_2[0]
        y_rec   = list_2[1]
        width   = list_2[2]
        height  = list_2[3]

        if (x > x_rec and x < (x_rec + width)) and (y > y_rec and y < (y_rec + height)):
            return True
        else:
            return False
    else:
        check_length = False
        

test_case = is_inside([200, 120], [140, 60, 100, 200])

if test_case ==  True:
    print("Your function is correct")
else:
    print("Oops, Bugs detected")

\