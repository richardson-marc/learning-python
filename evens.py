def myfunc(*args):
    evens = []
    for i in (args):
        if i % 2 ==0:
            evens.extend([i])
    return(evens)
