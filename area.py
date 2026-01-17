import math
import sys

if len(sys.argv[radius] == 1) :
    radius = sys.argv[1]
else:
    radius = 5

area = math.pi * radius * radius

print(area)
