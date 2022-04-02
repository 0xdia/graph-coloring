import sys

from graph import graph
from exact_methods.branch_and_bound import measured_branch_and_bound

if __name__ == "__main__":
    # Check the validity of the usage.
    if len(sys.argv) != 2:
        print("error: wrong number of arguements.")
        print("usage: python3 main.py input_file.txt\n")
        exit()

    input_file = sys.argv[1]

    # Create a graph from the input file.
    g = graph()
    g.read(input_file)

    # Color the graph g and mesure the time it takes.
    measured_branch_and_bound(g, False, True)
