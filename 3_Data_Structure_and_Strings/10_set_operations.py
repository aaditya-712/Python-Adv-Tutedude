
set1 = {1,2,3,4,5,6}
set2 = {1,3,5,6}

# & operator to get common elements from sets
print(set1 & set2)

# union - to get all unique elements from sets
print(set1.union(set2))

# issubset()
print(set2.issubset(set1))