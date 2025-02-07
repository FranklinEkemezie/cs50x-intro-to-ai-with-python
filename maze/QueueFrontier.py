
from Frontier import Frontier

class QueueFrontier(Frontier):
    """Represents a Frontier data structure
    implemented using a Queue data structure"""
    
    def remove(self):
        """Remove a node from the frontier"""

        if len(self.nodes) == 0:
            raise Error("Cannot remove a node from an empty frontier")

        # Get the first node
        node = self.nodes[0]

        # Update the nodes, removing the first node
        self.nodes = self.nodes[1:]

        # Return the node removed
        return node


