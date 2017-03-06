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
    return power(b, power(n, -1))
print(root(-1, 2))