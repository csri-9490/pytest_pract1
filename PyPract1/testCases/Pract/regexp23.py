import re
#A string containing no whitespace characters
str=str(input())
if re.search(r'^[A-Za-z0-9]*$',str):
    print('A string contains only word characters')
elif re.search(r'^\s*$',str):
    print('A string contains only space characters')
else:
    print('string containing both characters and spaces')

