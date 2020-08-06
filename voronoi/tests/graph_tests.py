import sys
import os

print(sys.path[0])
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from graph.coordinate import Coordinate
from graph.point import Point
from graph.algebra import Algebra

coord = Coordinate(2, 2)
assert coord.x == 2
assert coord.y == 2

point1 = Point(1, 0, None, 'firstPoint', None)
assert point1.name == 'firstPoint'

point2 = Point(0, 0, None, 'secondPoint', None)

dist = Algebra.distance(point1, point2)
assert dist == 1.0

vector = [4, 0]
norm = Algebra.magnitude(vector)
assert norm == 4.0

print('All graph tests passed')


