import arithmetic
import irrational
def sin(x, unit):
    if unit == "degrees":
        x = x*irrational.pi()/180
    print(x)
print(sin(20))

