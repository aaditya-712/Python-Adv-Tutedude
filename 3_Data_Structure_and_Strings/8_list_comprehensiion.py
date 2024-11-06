
# x = []
# for i in range(11):
#     if i%2 == 0:
#         z = i ** 2
#         x.append(z)
# print(x)


# list comprehension
#syntax: [expression for item in list/range if (test expression)]
x = [i ** 2 for i in range(11) if (i%2 == 0)]
print(x)
