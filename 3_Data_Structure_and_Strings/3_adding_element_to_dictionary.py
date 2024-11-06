# adding new element to dictionary
my_dict = {'a':'apple','b':'banana','c':'carrot','d':'dragonfriut'}
print(my_dict)

#adding
print("\nAdding new element")
my_dict['e'] = 'elephant'
print(my_dict)

#overwriting
print("\nOverwriting on existing element")
my_dict['a'] = 'animal'
print(my_dict)

#deleting
print("\nDeleting element")
del(my_dict['c'])
print(my_dict)

#boolean
print("\nChecking boolean")
print('b' in my_dict)
print('v' in my_dict)

#printing keys in dictionary
print("\nKeys in dictionary")
print(my_dict.keys())

#print values
print("\nvalues in dictionary")
print(my_dict.values())

#check if it is present
print("\nCheck if some key is present or not")
print(my_dict.get('g', "'g' not found"))