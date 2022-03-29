import sys

from graph import graph
from exact_methods.dynamic_programming import measure_execution_time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error: wrong number of arguements.")
        print("usage: python3 main.py input_file.txt\n")
        exit()

    input_file = sys.argv[1]

    g = graph()
    g.read(input_file)
    measure_execution_time(g)
    print("number of vertices: ", g.num_vertices, " number of edges: ", len(g.edges))
    print("NUmber of colors: ", g.approximative_optimum)
    print("Coloring: ", g.colors)
    print("Solution accepted ? ", g.validate_solution())
