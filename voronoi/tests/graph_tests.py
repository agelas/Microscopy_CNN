import sys
import os

print(sys.path[0])
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from graph.coordinate import Coordinate
from graph.point import Point

coord = Coordinate(2, 2)
assert coord.x == 2
assert coord.y == 2

point1 = Point(3, 3, None, 'firstPoint', None)
assert point1.name == 'firstPoint'

print('All graph tests passed')


