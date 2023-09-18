import math
def factorial(n):
    # n=int(input())
    fact=1
    if n<0:
        print('factorial not there for negative values')
    elif n==0:
        print('factrial of 0 is 1')
    else:
        for i in range(1,n+1):
            fact=fact*i
    return fact

def log10(m):
    return math.log10(m)

def degreetoradians(degrees):
    return math.radians(degrees)

def sincostan_values(angle):
    return math.sin(angle),math.cos(angle),math.tan(angle)

