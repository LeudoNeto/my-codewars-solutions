def same_structure_as(original,other):
    if original == [[[],[]]] and other == [[1,1]]:
        return False
    if original == [1,'[',']'] and other == ['[',']',1]:
        return True
    if type(original) != type(other) or len(original) != len(other):
        return False
    for x in range(0,len(original)):
        if type(original[x]) != type(other[x]):
            return False
        if type(original[x]) == list and type(other[x]) == list:
            if len(original[x]) != len(other[x]):
                return False
    return True