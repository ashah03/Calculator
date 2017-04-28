import sys
import arithmetic
def e():
    a = 1
    ans = 1
    for i in range(100):
            ans += 1 / arithmetic.factorial(a)
            a += 1
    return round(ans, 14)
def pi():
    pi = 3
    a = 2
    b = 3
    c = 4
    d = 5
    e = 6
    for i in range(1000000):
        pi = pi + 4.0 / (a * b * c) - 4.0 / (c * d * e)
        a += 4
        b += 4
        c += 4
        d += 4
        e += 4
    return round(pi, 14)
