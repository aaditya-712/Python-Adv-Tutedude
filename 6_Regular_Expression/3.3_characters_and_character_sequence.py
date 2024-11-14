# CHARACTERS AND CHARACTER SEQUENCE

# []
# [aeiou] - Matches a single character in the listed set
# [^xyz] - Matches a single character
# [a-z 0-9] - set of character can include a range
# {}

'''
import re
string = "pythonn"
# pattern = "[]"  #throws an error
# pattern = "[aeiou]"     #['o']
# pattern = "[^xyz]"      #['p', 't', 'h', 'o', 'n']
# pattern = "[a-z 0-9]"       #['p', 'y', 't', 'h', 'o', 'n']
pattern = "python{1}"       #['pytho']
print(re.findall(pattern, string, flags=0))
'''


import re
string = "From bobby.mark@mail.com"
pattern = "(@[^ ]*)"
print(re.findall(pattern, string, flags=0))