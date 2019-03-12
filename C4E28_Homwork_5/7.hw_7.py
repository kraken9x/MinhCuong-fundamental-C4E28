
def remove_dollar_sign(s):

    new_string = s.replace("$", "")
    return new_string

string = "$Techkid Coding$ $School"

display = remove_dollar_sign(string)
print(display)