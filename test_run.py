from voronoi.fortune_algorithm import Algorithm
from voronoi import BoundingBox
from voronoi import Polygon

polygon = BoundingBox(-10, 10, -10, 10)

# Points
points = [
    (-4, 7),
    (0, 5),
    (5, 0),
    (-5, -5),
    (7, -7)
]

v = Algorithm(polygon)
v.create_diagram(points=points, vis_steps=True, verbose=True, vis_result=True, vis_tree=True, vis_before_clipping=True)