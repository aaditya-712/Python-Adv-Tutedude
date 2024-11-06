try:
    a = 2
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("There is an error")
finally:
    print("continue with the code")