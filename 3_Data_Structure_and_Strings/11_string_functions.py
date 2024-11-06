a = "aadItyA"
print(a.capitalize())
print(a.upper())
print(a.lower())

b = '7'
print(b.isnumeric())
print(b.isalpha())

c = "Tommy is a good dog."
print(c.startswith('Tommy'))
print(c.endswith('dog.'))
print(c.replace('Tommy', 'Pug'))

d = "Pug is a good dog."
#    01234567
print(d.find('a'))

e = "   Pug is a good dog."
print(e)
print(e.lstrip())
# lstrip() - to strip space of left side
# rstrip() - to strip space of right side

#split
print(e.split())        #['Pug', 'is', 'a', 'good', 'dog.']
print(e.splitlines())

f = 'Ram', 'Sham'
print(f)
g = ','
print(g.join(f))