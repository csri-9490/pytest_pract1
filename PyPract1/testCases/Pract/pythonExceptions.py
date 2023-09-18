import time
def nameErrormsg():
	try:
		name = "namegiven"
		return sample
	except NameError as e:
		return "This statement is raising an NameError exception.",e

print(nameErrormsg())

def arithmeticError():
    try:
        a=10/0
    except ArithmeticError as e:
        return "This statement is raising an arithmetic exception.",e
print(arithmeticError())


def keyboardError():
 try:
    name=input("enter name:")
    return "You entered: " + name
 except KeyboardInterrupt:
    return "You hit control-c"
print(keyboardError())
