import math
import sys

if len(sys.argv) == 2:
    radius = float(sys.argv[1])
else:
    radius = 5

area = math.pi * radius * radius
print(area)