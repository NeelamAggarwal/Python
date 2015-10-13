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


# Customer 2: Local Rubber Sheet Co.
