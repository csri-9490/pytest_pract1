import re
pattern = r"^\S*$"

#A string that contains only whitespace characters or word characters
strings = ["HelloWorld", "NoWhitespace", "Has Space", "Only\tTabs", "Multiple Spaces"]
for s in strings:
    if re.match(pattern, s):
        print(f"String '{s}' contains no whitespace characters.")
    else:
        print(f"String '{s}' contains whitespace characters.")
