import re
#a.Digit at the beginning of the string and a digit at the end of the string
pattern = r'^\d.*\d$'
strings = ["1abc9", "0xyz0", "a123b", "42", "x123x"]
for s in strings:
    if re.match(pattern, s):
        print(f"String '{s}' matches the Digit at the beginning and end of the string pattern.")
    else:
        print(f"String '{s}'  does not match the Digit at the beginning and end of the string pattern.")

#b.A string that contains only whitespace characters or word characters
#c. A string containing no whitespace characters
strings1 = ["HelloWorld", "NoWhitespace", "Has Space", "Only\tTabs", "Multiple Spaces","    "]
for str in strings1:
    if re.search(r'^[A-Za-z0-9]*$',str):
     print(str,'A string contains only word characters')
    elif re.search(r'^\s*$',str):
     print(str,'A string contains only space characters')
    else:
     print(str,'string containing both characters and spaces')



