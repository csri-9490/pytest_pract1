n=int(input())
temp=n
l1=len(str(n))
rev=0

while temp>0:
	digit=temp%10
	rev=rev+digit**l1
	temp=temp//10
print(rev)