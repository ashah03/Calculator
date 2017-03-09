import arithmetic
import irrational
pi = irrational.pi()
def sin(x, unit):
    if unit == "degrees":
        x = x*pi/180

print(sin(20, "degrees"))

