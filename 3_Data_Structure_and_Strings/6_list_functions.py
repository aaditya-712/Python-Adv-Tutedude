l = ['mike', 1.02, 2003]

#adding an element to list --> append (can only add one value at a time)
l.append(10)
print(l)

#adding element to list --> extend (can add multiple values at a time)
l.extend([7, 12])
print(l)

#removing element from the list --> remove (can remove 1 value at a time)
l.remove(7)
print(l)

# del - can remove multiple values at a time
del l[0:2]
print(l)

# clear - makes the list blank list
l.clear()
print(l)

l = ['mike', 1.02, 2003, 10, 12]

# pop - another way to delete an element by index
l.pop(2)
print(l)

# insert - adds element at specific index
l.insert(2, "aadi")
print(l)

num = [2003, 365.5, 10, 12]

# sort - arrange in ascending order
num.sort()
print(num)

# reverse - reverse the list as it is
num.reverse()
print(num)

# index - to check index value of element
print(num.index(10))

# len - length of the list
print(len(num))

