import sys
from graph import graph
from meta_heuristics.grey_wolf_optimizer.grey_wolf_optimizer import GWO

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
    # file_name = input_file.split("\\")[-1].split(".")[0]
    # Colorer le graphe g et mesure le temps que ça prend.
    # choisir une algorithe et l'appeler ici
    GWO(g, 300, 50)
