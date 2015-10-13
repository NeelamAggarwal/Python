"""Copyright (c) 2015 Circuitous(tm), all rights reserved.

Erick Ries author of the Lean Startup Method.
Lean Startup Method : Business Plans :: Agile : Waterfall

YAGNI ... Ya Ain't Gonna Need It
"""

from collections import namedtuple

Version = namedtuple('Version', 'major minor')


class Circle:
    "An advanced circle analytics toolkit"

    version = Version(0, 1)

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2
