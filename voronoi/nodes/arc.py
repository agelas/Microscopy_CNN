from graph.coordinate import Coordinate

class Arc:
    '''
    Each leaf of the beach line, representing an arc alpha, stores one pointer
    to a node in the event queue. That node represents the circle event that makes
    arc alpha disappear. Pointer is None if no circle event exists, or the circle
    event has not been detected yet
    '''

    def __init__(self, origin: Coordinate, circle_event = None):
        '''
        param origin: The point that caused the arc
        param circle_event: The pointer to the circle event in which the arc
        will disappear
        '''
        self.origin = origin
        self.circle_event = circle_event

    def __repr__(self):
        return f"Arc({self.origin.name})"

    def get_plot(self, x, sweep_line):
        '''
        Function for plotting the arc.
        param x: The input x-coordinates (literally points, not the class Coordinate)
        param sweep_line: The y-coordinate of the sweep line
        return: A list of y-values
        '''
        sweep_line = sweep_line
        i = self.origin

        if i.y - sweep_line == 0:
            return None
        
        u = 2 * (i.y - sweep_line)
        v = (x ** 2 - 2 * i.x * x + i.x ** 2 + i.y ** 2 - sweep_line ** 2)
        y = v/u

        return y