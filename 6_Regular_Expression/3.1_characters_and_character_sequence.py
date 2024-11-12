# CHARACTERS AND CHARACTER SEQUENCE

# ^ - Matches the beginning of the line
# $ - Matches the end of line
# . - Matches any character
# \d - Matches any digit
# \D - Matches any non-digit
# \s - Matches any whitespace
# \S - Matches any non-whitespace
# --------------------------------------------------------

# ^ - Matches the beginning of the line
# import re
# string = "It is a dog"
# pattern = "^I"
# print(re.findall(pattern, string, flags=0))

# --------------------------------------------------------

# $ - Matches the end of line
# import re
# string = "It is a dog"
# pattern = "g$"
# print(re.findall(pattern, string, flags=0))

# --------------------------------------------------------

# . - Matches any character
# import re
# string = "It is a dog"
# pattern = "^...."
# print(re.findall(pattern, string, flags=0))

# --------------------------------------------------------

# \d - Matches any digit
# import re
# string = "It is a dog 23"
# pattern = "\d"
# print(re.findall(pattern, string, flags=0))

# --------------------------------------------------------

# \D - Matches any non-digit
# import re
# string = "It is a dog 23"
# pattern = "\D"
# print(re.findall(pattern, string, flags=0))

# --------------------------------------------------------

# \s - Matches any whitespace
# import re
# string = "It is a dog 23"
# pattern = "\s"
# print(re.findall(pattern, string, flags=0))

# --------------------------------------------------------

# \S - Matches any non-whitespace
import re
string = "It is a dog 23"
pattern = "\S"
print(re.findall(pattern, string, flags=0))

