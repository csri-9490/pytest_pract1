#7.Implement a simple generator for Fibonacci series
def fibonacci_Generator():
    a = 0
    b = 1
    for i in range(6):
        yield b
        a, b = b, a + b
obj = fibonacci_Generator()
for i in range(6):
    print(next(obj))
