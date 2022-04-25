import sys

from graph import graph
from heuristics.RLF import rlf
from exact_methods.branch_and_bound import branch_and_bound_recursive

if __name__ == "__main__":
    # Vérifier la validité d'usage.
    if len(sys.argv) != 2:
        print("error: wrong number of arguements.")
        print("usage: python3 main.py input_file.txt\n")
        exit()

    input_file = sys.argv[1]

    # Créer un graphe à partir du fichier d'entrée.
    g = graph()
    g.read(input_file)

    # Colorer le graphe g et mesure le temps que ça prend.
    rlf(g)
    # branch_and_bound_recursive(g, False)

    print("result is: ")
    print(g.optimum)
    print(g.colors)
    g.validate_solution()
    # g.visualize_graph()
