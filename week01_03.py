import sys
import math
import cmath

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - 4*a*c
try: d = math.sqrt(d)
except:
    d = cmath.sqrt(d)
x1 = int((-b + d) / (2 * a))
x2 = int((-b - d) / (2 * a))
print (x1)
print (x2)


