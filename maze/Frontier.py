
class Frontier:
    """Represents a Frontier data structure"""
    
    def __init__(self):
        self.nodes = []


    def add(self, node):
        """Add a node to the frontier"""

        self.nodes.append(node)


    def remove(self):
        """Remove a node from the frontier"""

        raise Error("No implementation for method. Use any of the same method implemented in concrete classes e.g. StackFrontier, QueueFrontier")


    def empty(self):
        """Checks if the frontier is empty"""

        return len(self.nodes) == 0
    

    def has_node(self, node):
        """Check whether the node is contained in the frontier"""

        node_x, node_y = node.state

        for n in self.nodes:

            n_x, n_y = n.state
            if n_x == node_x and n_y == node_y:
                return True

        return False
