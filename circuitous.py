"""Copyright (c) 2015 Circuitous(tm), all rights reserved.

Erick Ries author of the Lean Startup Method.
Lean Startup Method : Business Plans :: Agile : Waterfall

YAGNI ... Ya Ain't Gonna Need It
"""

from collections import namedtuple
import math

Version = namedtuple('Version', 'major minor')


class Circle(object):
    "An advanced circle analytics toolkit"

    version = Version(0, 4)

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * self.radius * 2
