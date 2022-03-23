import sys
from graph import graph
from exact_methods.branch_and_bound import measure_execution_time

if __name__ == "__main__":
    if len(sys.argv) != 4:
        if len(sys.argv) < 4:
            print("error: too few arguements.")
        else:
            print("error: too many arguements.")
        print(
            "usage: python3 main.py input_file (--adjlist | --edges) (--0-indexed | --1-indexed)\n"
        )
        exit()

    if (sys.argv[-2] not in ["--adjlist", "--edges"]) or (sys.argv[-1] not in ["--0-indexed", "--1-indexed"]):
        print(
            "usage: python3 main.py input_file (--adjlist | --edges) (--0-indexed | --1-indexed)\n"
        )
        exit()

    
    input_file = sys.argv[1]
    mode = sys.argv[2]
    indexation = sys.argv[3]

    g = graph()
    g.read(input_file, mode, indexation)
    measure_execution_time(g)
    g.visualize_graph()
