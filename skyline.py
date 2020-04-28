def myfunc(string):
    ret = []
    i = True
    for char in string:
        if i:
            ret += char.lower()
        else:
            ret += char.upper()
        if char != ' ':
            i = not i
    return ret
