
from Frontier import Frontier

class StackFrontier(Frontier):
    """Represents a Frontier data structure
    implemented using a Stack data structure"""

    def remove(self):
        """Remove a node from the frontier"""

        if len(self.nodes) == 0:
            raise Error("Cannot remove a node from an empty frontier")
        # Get the last node
        node = self.nodes[-1]

        # Update the nodes, removing the laat node
        self.nodes = self.nodes[:-1]

        # Return the node removed
        return node
       



