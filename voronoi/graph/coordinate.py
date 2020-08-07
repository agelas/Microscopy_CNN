class Coordinate:
    def __init__(self, x=None, y=None):
        '''
        A point in a 2D coordinate system
        '''
        self.x: float = x
        self.y: float = y

    def __repr__(self):
        '''
        returns object representation of a Coordinate
        '''
        return f"({round(self.x, 3)}, {round(self.y, 3)})"
    