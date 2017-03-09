import arithmetic
import irrational

pi = irrational.pi()
def d2r(deg):
    return deg * pi / 180
def sin(x, unit):
    if unit == "degrees":
        x = d2r(x)
    a = 1
    b = 3
    ans = 0
    for i in range(10): #Taylor series for sin(x)
        ans += (arithmetic.power(x, a))/arithmetic.factorial(a) #Adding term
        ans -= (arithmetic.power(x, b))/arithmetic.factorial(b) #Subtracting term
        a+=4 #Every other term
        b+=4
    return round(ans, 9)


def cos(x, unit):
    if unit == "degrees":
        x = d2r(x)
    a = 2
    b = 4
    ans = 1
    for i in range(10):
            ans -= arithmetic.power(x, a) / arithmetic.factorial(a)
            ans += arithmetic.power(x, b) / arithmetic.factorial(b)
            a += 4
            b += 4
    return round(ans, 9)

def tan(x, unit):
    if unit == "degrees":
        x = d2r(x)
    return round(sin(x,"radians")/cos(x,"radians"), 9)

