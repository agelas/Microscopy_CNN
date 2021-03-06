import sys
import os

print(sys.path[0])
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from graph.coordinate import Coordinate
from graph.point import Point
from graph.algebra import Algebra

#Test that a Coordinate can initialize correctly
coord = Coordinate(2, 2)
assert coord.x == 2
assert coord.y == 2

#Test that a Point can initialize correctly
point1 = Point(1, 0, None, 'firstPoint', None)
assert point1.name == 'firstPoint'

#Test Algebra.distance(point_1, point_2) calculates correct distance
point2 = Point(0, 0, None, 'secondPoint', None)
dist = Algebra.distance(point1, point2)
assert dist == 1.0

#Test Algebra.magnitude(vector) calculates correct magnitude of a vector
vector = [4, 0]
magnitude = Algebra.magnitude(vector)
assert magnitude == 4.0

#Test Algebra.norm(vector) calculates correct norm of a vector
norm = Algebra.norm(vector)
normSum = sum(norm)
assert normSum == 1.0

print('All graph tests passed')


