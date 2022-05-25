import sys
from graph import graph
from meta_heuristics.genetic_algorithm import (
    genetic_algorithm,
    measure_genetic_algorithm,
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
    measure_genetic_algorithm(
        g,
        pool_size=400,
        selection_strategy="roulette",
        selection_percentage=0.6,
        crossing_proba=0.8,
        crossing_manner="1",
        mutation_proba=0.5,
        nbr_iterations=25,
    )
    # Colorer le graphe g et mesure le temps que ça prend.

    g.validate_solution()
    # g.visualize_graph()
