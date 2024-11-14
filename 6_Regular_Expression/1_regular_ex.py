# regular expression
# mostly used for strings
# import re (to use regular expression)
# validiate the input


# 1: match(pattern. string, flags)
# import re
# pattern = "apple"
# if re.match(pattern, "apple"):
#     print("matched")
# else:
#     print("not matched")


# 2: findall(pattern, string, flags)
# import re
# pattern = "apple"
# string = re.findall("apple", pattern)
# print(string)


# 3: search(pattern, string, flags)
import re
pattern = "apple"
if re.search(pattern, "apple", flags=0):
    print("True")
else:
    print("False")
