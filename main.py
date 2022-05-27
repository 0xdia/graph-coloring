import sys
from graph import graph
from meta_heuristics.tabu_search import measure_tabu

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
    # measured_dp(g)
    # measure_rlf(g)
    # measure_d_satur(g)
    # measured_branch_and_bound(g, False, False)
    measure_tabu(g, 20)

    g.validate_solution()
    # g.visualize_graph()
