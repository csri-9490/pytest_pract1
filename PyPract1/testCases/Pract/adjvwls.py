import  re
l1='srikanrth redddy chsfldf aei lklio ou kjkk'
vw=['a','e','i','o','u']
# for word in l1.split():
#     s1=re.findall(r'\b\w[aeiouAEIOU]{2}\w\b',l1)
# print(s1)

s=re.findall(r'\b\w[aeiouAEIOU]{2}\w\b',l1)
print(s)