
from Frontier import Frontier
from QueueFrontier import QueueFrontier
from StackFrontier import StackFrontier
from Node import Node

class Agent():
    """Represents an AI Agent"""
    
    def __init__(self):
        self.maze = None


    def solve(self, maze, bfs=True):

        # Set the maze
        self.maze = maze

        # Initial state node
        initial_node = Node(maze.initial)

        # Start with a frontier that contains the initial state
        frontier = QueueFrontier() if bfs else StackFrontier()
        frontier.add(initial_node)
        print("Initialised frontier for", "BFS" if bfs else "DFS", "...\n")

        # Repeat
        while True:
            
            # If the frontier is empty, then no solution
            if frontier.empty():
                return None

            # Remove a node from the frontier
            node = frontier.remove()

            # If node contains goal state, return the solution
            if maze.is_goal(node):
                print("Solution found!")
                print(f"Nodes explored: {len(maze.explored_nodes)}")


                return node


            # If node does not contain goal state, add to the explored set
            maze.add_explored_node(node)


            # Expand node, add resulting nodes if they are not in the frontier or the explored set
            for n in maze.get_explorable_nodes(node):
                if not frontier.has_node(n) and not maze.is_node_explored(n):
                    frontier.add(n)


    def describe_path(self, maze, goal, output_filename):
        """Describe the path taken to solve the maze"""

        # Get the maze but, with paths explored on it marked with '*'
        maze_sln = maze.show_path_on_maze()

        with open(output_filename, "w") as file:

            lines = [f"{"".join(row)}\n" for row in maze_sln]
            file.writelines(lines)
