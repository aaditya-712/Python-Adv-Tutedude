# CHARACTERS AND CHARACTER SEQUENCE

# * - Repeats a character zero or more times
# + - Repeats a character one or more times
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end
# ? - Matches the expression 0 to 1 times

# --------------------------------------------------------

# * - Repeats a character zero or more times
# import re
# string = "From bobby.mark@gmail.com"
# pattern = "ma*"
# print(re.findall(pattern, string))

# --------------------------------------------------------

# + - Repeats a character one or more times
# import re
# string = "From bobby.mark@gmail.com"
# pattern = "ma+"
# print(re.findall(pattern, string))

# --------------------------------------------------------

# ( - Indicates where string extraction is to start
import re
string = "From bobby.mark@gmail.com"
pattern = "^From (\S"
print(re.findall(pattern, string))

# --------------------------------------------------------

# ? - Matches the expression 0 to 1 times
# import re
# string = "From bobby.mark@gmail.com"
# pattern = "^F.*?"
# pattern1 = "^F.+?"
# print(re.findall(pattern, string))
# print(re.findall(pattern1, string))
