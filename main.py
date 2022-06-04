import sys
from graph import graph

from meta_heuristics.tabu_search import measure_tabu

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

    # Colorer le graphe g et mesure le temps que ça prend.
    # choisir une algorithe et l'appeler ici
    measure_genetic_algorithm(g, 200, "roulette", 0.5, 0.5, "uniform", 0.5, 100)
