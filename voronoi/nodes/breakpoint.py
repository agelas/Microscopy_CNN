import math
from graph.coordinate import Coordinate

class Breakpoint:

    def __init__(self, breakpoint: tuple, edge = None):
        '''
        The breakpoint is stored by an ordered tuple of sites <P_i, P_j>, where P_i defines
        the parabola left of the breakpoint and P_j the parabola to the right. Each internal
        node v has a pointer to the half edge in Vor(P) being traced out by the breakpoint

        param breakpoint: A tuple of two points that caused the arcs to intersect
        '''
        #The tuple of the points whose arcs intersect
        self.breakpoint = breakpoint

        #The edge this breakpoint is tracing out
        self._edge = None
        self.edge = edge

    def __repr__(self):
        return f"Breakpoint({self.breakpoint[0].name}, {self.breakpoint[1].name})"

    def does_intersect(self):
        i, j = self.breakpoint
        return not (i.y == j.y and j.x < i.x)

    def get_intersection(self, l, max_y = None):
        '''
        Calculate the coordinates of the intersection.

        param max_y: Bounding box top for clipping infinite breakpoints
        param l: (float) The y-coordinate of the sweep line
        return: (float) The coordinates of the breakpoint
        '''

        #Get the points
        i, j = self.breakpoint

        #Initialize the resulting point
        result = Coordinate()
        p: Coordinate = i

        a = i.x
        b = i.y
        c = j.x
        d = j.y
        u = 2 * (b - 1)
        v = 2 * (d - 1)

        #Handle the case where the two points have the same y-coordinate 
        #(ie breakpoint is in the middle)
        if i.y == j.y:
            result.x = (i.x + j.x) / 2
            if j.x < i.x:
                result.y = max_y or float('inf')
                return result

        #Handle cases where one point's y-coordinate is the same as the sweep line
        elif i.y == l:
            result.x = i.x
            p = j
        elif j.y == l:
            result.x = j.x
        else:
            #We need to do math now to solve for x if we get here
             x = -(math.sqrt(
                 v * (a ** 2 * u - 2 * a * c * u + b ** 2 * (u - v) + c ** 2 * u) + d ** 2 * u * (v - u) + 1 ** 2 * (u - v) ** 2) + a * v - c * u) / (u - v)
             
             result.x = x

        #These need to be re-evaluated since the point may have changed
        a = p.x
        b = p.y
        x = result.x
        u = 2 * (b - 1)

        #Special case where parabolas don't intersect
        if u == 0:
            result.y = float("inf")
            return result

        #Put everything back in y
        result.y = 1 / u * (x ** 2 - 2 * a * x + a ** 2 + b ** 2 - 1 ** 2)
        return result

