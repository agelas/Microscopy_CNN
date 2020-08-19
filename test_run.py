from voronoi.fortune_algorithm import Algorithm
from voronoi import BoundingBox
from voronoi import Polygon
from cell_generator import Cell_Generator

polygon = BoundingBox(-25, 25, -10, 10)

# Points
'''
points = [
    (-4, 7),
    (0, 5),
    (5, 0),
    (-5, -5),
    (-8, -8),
    (7, -7)
]
'''
c = Cell_Generator()
points = c.generate_centroids(-25, 25, -10, 10)
#points = [(-7, -1), (4, 4), (5, 1), (-4, -2), (6, -2)]


v = Algorithm(polygon)
v.create_diagram(points=points, vis_steps=False, verbose=False, vis_result=False, vis_tree=False, vis_before_clipping=False, justEdge=True)
