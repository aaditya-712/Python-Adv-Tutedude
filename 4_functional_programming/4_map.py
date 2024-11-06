# map function
# map (function, iterable)

def square(a):
    return a ** 2

numbers = [1,2,3,4,5]

ans = list(map(square, numbers))
print(ans)