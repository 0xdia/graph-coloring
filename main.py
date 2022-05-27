import sys
from graph import graph

from meta_heuristics.genetic_algo_params_tuning import (
    pool_size_impact,
    num_generations_impact,
    mutation_probability_impact,
    crossing_probability_impact,
)

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

    crossing_probability_impact(g)
