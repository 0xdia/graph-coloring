import sys
from graph import graph
from exact_methods.branch_and_bound import measured_branch_and_bound
from exact_methods.dynamic_programming import measured_dp
from heuristics.RLF import measure_rlf
from heuristics.d_satur import measure_d_satur
from metaheuristics.tabu_search import measure_tabu

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
    #measured_dp(g)
    #measure_rlf(g)
    #measure_d_satur(g)
    #measured_branch_and_bound(g, False, False)
    measure_tabu(g)

    g.validate_solution()
    #g.visualize_graph()
