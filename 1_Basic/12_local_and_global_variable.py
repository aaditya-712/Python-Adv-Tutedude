n = 1    # GLOBAL VARIABLE

def fn():
    n = 5   # LOCAL VARIABLE
    print("in ", n)


fn()
print("out ", n)