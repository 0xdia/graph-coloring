import sys

from graph import graph
from exact_methods.branch_and_bound import measure_execution_time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error: wrong number of arguements.")
        print("usage: python3 main.py input_file.txt\n")
        exit()

    input_file = sys.argv[1]

    g = graph()
    g.read(input_file)
    measure_execution_time(g, False)
    g.visualize_graph()
