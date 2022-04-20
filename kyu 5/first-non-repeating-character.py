def first_non_repeating_letter(string):
    string2 = string.lower()
    for x,y in enumerate(string2):
        if string2.count(y) == 1:
            return string[x]
    return ''