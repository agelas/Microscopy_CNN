from tree.smart_node import SmartNode

class InternalNode(SmartNode):
    '''
    Is basically a SmartNode. Internal nodes store the breakpoints on the beach
    line.
    '''

    def __init__(self, data: "BreakPoint"):
        super().__init__(data)

    def __repr__(self):
        return f"Internal({self.data}, left = {self.left}, right = {self.right})"

    def get_key(self, sweep_line = None):
        return self.data.get_intersection(sweep_line).x

    def get_value(self, **kwargs):
        return self.data

    def get_label(self):
        return f"{self.data.breakpoint[0].name}{self.data.breakpoint[1].name}"