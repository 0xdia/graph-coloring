import sys
from graph import graph

from meta_heuristics.tabu_search import measure_tabu

from meta_heuristics.genetic_algorithm import (
    genetic_algorithm,
    measure_genetic_algorithm,
)

from meta_heuristics.genetic_algo_params_tuning import crossing_probability_impact

from exact_methods.branch_and_bound import measured_branch_and_bound

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
    file_name = input_file.split("/")[-1].split(".")[0]
    # Colorer le graphe g et mesure le temps que ça prend.
    # choisir une algorithe et l'appeler ici

    crossing_probability_impact(g, file_name)
