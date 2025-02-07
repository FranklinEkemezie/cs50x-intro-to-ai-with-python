import argparse

from Agent import Agent
from Maze import Maze

parser = argparse.ArgumentParser(
    description="A simple Python script to solve a maze"
)


# Add the necessary arguments

parser.add_argument(
    "filename",
    type=str,
    help="The maze file"
)
parser.add_argument(
    "--search",
    "-s",
    choices=["bfs", "dfs"],
    default="bfs",
    help="The type of search algorithm to use"
)
parser.add_argument(
    "--img",
    "-i",
    action="store_false",
    help="Save image for the solution found"
)

# Set defaults
parser.set_defaults(img=False)

# Parse the arguments
args = parser.parse_args()


# Load the maze into memory
maze = Maze(args.filename)

# Initiate an AI agent
agent = Agent()

# Solve the maze
goal = agent.solve(maze, args.search == "bfs")

# Describe the path used to solve the maze
output_filename = "maze_files/maze1_sln.txt"
agent.describe_path(maze, goal, output_filename)
