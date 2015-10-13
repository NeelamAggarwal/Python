"""circuitous_client.py
The customers' code.
"""

from circuitous import Circle
from random import random, seed

### Customer 1: Our Academic Friends ######

print 'Proposal to research the areas'
print 'of random circles'
print "seeded with Jenny's number"
seed(8675309)
print 'using Circuitous(tm)'
print Circle.version
n = 10
circles = [Circle(random()) for i in range(10)]
areas = [c.area() for c in circles]
print 'the average area of', n, 'circles'
print 'is %.2f' % (sum(areas) / n)
print

# Customer 2: Local Rubber Sheet Co.

cuts = [0.3, 0.7, 0.2]
circles = [Circle(radius) for radius in cuts]
for c in circles:
    print 'a circle of radius', c.radius
    print 'has an cold area', c.area()
    print 'and a perimeter', c.perimeter()
    c.radius *= 1.1
    print 'and a warm area', c.area()
    print


# Customer 3: Regional Tire Co.

class Tire(Circle):

    def perimeter(self):
        "adjusted perimeter for width of tire"
        return Circle.perimeter(self) * 1.25

t = Tire(22)
print 'a tire with radius', t.radius
print 'has an area', t.area()
print 'and a perimeter', t.perimeter()
