def add(a, b):
    return a + b
def subtract(a, b):
    return add(a, -b)
def multiply(a, b):
    return a*b
def divide(a, b):
    if b == 0:
        return "Undefined"
    else:
        return multiply(a, power(b, -1))
def power(b, x):
    return b**x
def root(b, n):
    if n == 2:
        return sqrt(b)
    else:
        return power(b, power(n, -1))
def sqrt(a):
    x = 10
    b = abs(a)
    for i in range(100):
        x = ((x + (b / x)) / 2)
    if a >= 0:
        return x
    else:
        return complex(0, x)

