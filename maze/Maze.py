
import os


class Maze:
    """Represents a maze as described in the maze text file""" 


    def __init__(self, maze_filename):

        if not os.path.exists(maze_filename):
            raise FileNotFoundError(f"{maze_filename} not found")

        self.filename = maze_filename
        self.maze = [] # 2D structure representing maze
        self.initial = False
        self.goal = False
        self.explored_nodes = []

        # Build the maze in memory
        self.build()


    def parse_maze_file(self):
        """Parse the maze file returning the maze as a 2D array"""

        width = height = 0
        maze_lines = []

        with open(self.filename, "r") as file:

            line = file.readline()
            while line:
                if line[-1] == "\n": 
                    # remove trailing whitespaces
                    line = line[:-1]

                line_width = len(line)

                width = line_width if line_width > width else width
                height += 1

                maze_lines.append(line)

                line = file.readline()

        # Adjust with of maze by padding
        maze = [list(line.rjust(width, ' ')) for line in maze_lines]

        return maze


    def get_initial_and_goal_state(self):

        initial = None
        goal = None

        for y, row in enumerate(self.maze):
            for x, block in enumerate(row):

                if block == 'A':
                    initial = (x, y)

                if block == 'B':
                    goal = (x, y)

                if initial and goal:
                    break

        if not initial:
            raise Error("No initial state found")

        if not goal:
            raise Error("No goal state found")

        return initial, goal


    def build(self):

        print("Building maze in memory...")

        self.maze = self.parse_maze_file()

        initial, goal = self.get_initial_and_goal_state()
        self.initial = initial
        self.goal = goal

        print("Maze loaded successfully!")


    def can_explore_node(self, node):
        """Whether the given node is a path in the maze"""

        x, y = node.state

        try:
            return self.maze[y][x] in [' ', 'A', 'B']
        except:
            return False


    def get_explorable_nodes(self, node):
        """Get the nodes that can be explored
        from the given node"""

        nodes = []
        for node in node.get_surrounding_nodes():
            if self.can_explore_node(node):
                nodes.append(node)

        return nodes


    def is_goal(self, node):
        """Determine whether the node is a goal state"""
        goal_x, goal_y = self.goal
        node_x, node_y = node.state

        return goal_x == node_x and goal_y == node_y
 

    def is_initial(self, node):
        """Determine whether the node is an initial state"""

        init_x, init_y = self.initial
        node_x, node_y = node.state

        return init_x == node_x and init_y == node_y


    def add_explored_node(self, node):
        """Add a node to the explored set"""

        self.explored_nodes.append(node)


    def is_node_explored(self, node):
        """Determine whether the node has been explored"""

        node_x, node_y = node.state

        for n in self.explored_nodes:

            n_x, n_y = n.state
            if n_x == node_x and n_y == node_y:
                return True

        return False


    def show_path_on_maze(self):
        """Describe the path explored on the maze"""

        maze_sln = self.maze

        if self.explored_nodes == 0:
            return maze_sln

        action_map = {
            "N": "^",
            "S": "v",
            "W": "<",
            "E": ">"
        }

        for node in self.explored_nodes:

            if self.is_initial(node) or self.is_goal(node):
                continue

            x, y = node.state
            maze_sln[y][x] = action_map[node.action]

        return maze_sln


