
class Node:
    """Represents a Node data structure"""
    
    def __init__(self, state, action=None, parent=None, cost=1):
        self.state 	= state
        self.action = action
        self.parent = parent
        self.cost	= cost


   
    def get_surrounding_nodes(self):
        """Get the nodes which MAY surround the given node"""

        x, y = self.state

        # Get the four nodes which may surround the given node
        top     = Node((x, y-1), "N", self)
        bottom  = Node((x, y+1), "S", self)
        left    = Node((x-1, y), "W", self)
        right   = Node((x+1, y), "E", self)

        return top, bottom, left, right
