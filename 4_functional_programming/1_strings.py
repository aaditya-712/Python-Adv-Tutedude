def add(i, j):
    return i + j

def call(i, j):
    return add(i, j)

def pas(i, j, fn):
    return fn(i, j)

res = pas(1,2, call)
print(res)