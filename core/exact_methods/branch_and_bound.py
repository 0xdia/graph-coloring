import heapq
import time

# Garder une trace du nombre de fois que `search` est exécuté.
recursion_depth = 0


def branch_and_bound_recursive(g, return_on_first_leaf=False):
    """
    Implémentation récursive de l'algorithme de branch and bound pour
         résoudre le problème de coloration d'un graphe.
         * g : le graphe à colorer
         * return_on_first_leaf : un indicateur pour retourner lors de l'atteinte de la première solution.
    """

    def search(g, sub_coloring, num_colors, num_non_colored):
        """
        Fonction récursive pour évaluer un nœud interne dans l'arbre du parcours du branch and bound.
                 * g : le graphe à colorier.
                 * sub_coloring : le nœud interne.
                 * num_colors : nombre de couleurs utilisées dans ce nœud.
                 * num_non_colored : nombre de sommets non colorés dans ce nœud.
        """
        global recursion_depth
        recursion_depth += 1

        # Retourner si l'optimum a été mis à jour et que l'indicateur `return_on_first_leaf` est vrai.
        if return_on_first_leaf and g.optimum < g.num_vertices + 1:
            return

        # Mettre à jour le nombre optimal de couleurs et les couleurs des sommets de g
        # si une meilleure solution est trouvée.
        if num_non_colored == 0 and num_colors < g.optimum:
            g.optimum = num_colors
            g.colors = sub_coloring.copy()
            return

        # Couper la branche si le nombre de couleurs utilisées jusqu'à présent
        # est déjà supérieur ou égal à l'optimum.
        if num_colors >= g.optimum:
            return

        # Introduiser une nouvelle couleur.
        new_color = num_colors

        # Créer une liste pour contenir les fils de ce nœud.
        extended_sub_coloring = []

        # Créer des fils pour ce nœud.
        for i in range(len(sub_coloring)):
            # Trouver le prochain sommet non coloré.
            if sub_coloring[i] != -1:
                continue

            # Initialiser un nouveau fils.
            not_yet_colored = num_non_colored
            possibility = sub_coloring.copy()

            # Colorez le sommet non coloré trouvé avec la nouvelle couleur.
            possibility[i] = new_color
            not_yet_colored -= 1

            # Colorer autant de sommets que possible avec la nouvelle couleur.
            for j in range(len(possibility)):
                # Trouver le prochain sommet non coloré.
                if possibility[j] != -1:
                    continue

                # Colorer le sommet non coloré trouvé avec la nouvelle couleur
                # s'il n'y a pas de conflit avec les couleurs des voisines.
                neighbors_colors = g.get_neighbors_colors(j, possibility)
                if new_color not in neighbors_colors:
                    possibility[j] = new_color
                    not_yet_colored -= 1

            # Ajouter le nouveau fils à la liste.
            if (not_yet_colored, possibility) not in extended_sub_coloring:
                extended_sub_coloring.append((not_yet_colored, possibility))

        # Trier les fils par ordre croissant
        # en fonction de la valeur de not_yet_colored (le plus proche de la feuille).
        extended_sub_coloring.sort()

        # Appeler `search` sur chaque fils créé.
        for extended in extended_sub_coloring:
            search(g, extended[1], new_color + 1, extended[0])

    # Initialiser le nœud racine avec tous les sommet sans couleur.
    # Initialiser l'optimum avec une valeur supérieure au pire des cas.
    sub_coloring = [-1 for _ in range(g.num_vertices)]
    g.optimum = g.num_vertices + 1

    # Lancer la recherche.
    search(g, sub_coloring, 0, g.num_vertices)
    print("recursion_depth is; ", recursion_depth)


def branch_and_bound_iterative(g, return_on_first_leaf=False):
    """
    Iterative implimentation of branch and bound algorithm
    to solve the coloring problem in a graph
    * g: the graph to be colored
    * return_on_first_leaf: a flag to return when reaching the first solution.
    """
    # Initialiser l'optimum avec une valeur supérieure au pire des cas.
    g.optimum = g.num_vertices + 1

    # Créer une file d'attente avec priorité pour contenir les nœuds
    # avec les nœuds les plus proches du feuilles (ayant le moins de sommets non colorés),
    # et en utilisant moins de couleurs, dans cet ordre, ayant une priorité plus élevée.
    pq = []

    # Poussez le nœud racine vers la file d'attente.
    heapq.heappush(pq, (g.num_vertices, 0, [-1 for _ in range(g.num_vertices)]))

    # Tant que toutes les branches n'ont pas été évaluées.
    while len(pq) != 0:

        # Pop le nœud de priorité la plus élevée.
        num_non_colored, num_colors, sub_coloring = heapq.heappop(pq)

        # Retourner si l'optimum a été mis à jour et que l'indicateur `return_on_first_leaf` est vrai.
        if return_on_first_leaf and g.optimum < g.num_vertices + 1:
            break

        # Mettre à jour le nombre optimal de couleurs et les couleurs des sommets de g
        # si une meilleure solution est trouvée.
        if num_non_colored == 0 and num_colors < g.optimum:
            g.optimum = num_colors
            g.colors = sub_coloring.copy()
            continue

        # Introduiser une nouvelle couleur.
        new_color = num_colors

        # Créer des fils pour ce nœud.
        for i in range(len(sub_coloring)):
            # Trouver le prochain sommet non coloré.
            if sub_coloring[i] != -1:
                continue

            # Initialiser un nouveau fils.
            not_yet_colored = num_non_colored
            possibility = sub_coloring.copy()

            # Colorer le sommet non coloré trouvé avec la nouvelle couleur.
            possibility[i] = new_color
            not_yet_colored -= 1

            # Colorer autant de sommets que possible avec la nouvelle couleur.
            for j in range(len(possibility)):
                # Trouver le prochain sommet non coloré.
                if possibility[j] != -1:
                    continue

                # Colorer le sommet non coloré trouvé avec la nouvelle couleur
                # s'il n'y a pas de conflit avec les couleurs des voisines.
                neighbors_colors = g.get_neighbors_colors(j, possibility)
                if new_color not in neighbors_colors:
                    possibility[j] = new_color
                    not_yet_colored -= 1

            # Couper la branche si le nombre de couleurs utilisées jusqu'à présent
            # est déjà supérieur ou égal à l'optimum.
            if new_color + 1 >= g.optimum:
                continue

            # Ajouter le nouveau fils à la file d'attente.
            if not (not_yet_colored, new_color + 1, possibility) in pq:
                heapq.heappush(pq, (not_yet_colored, new_color + 1, possibility))

    return


def measured_branch_and_bound(g, return_on_first_leaf=False, recursive=False):
    """
    Mesurez le temps qu'il faut pour colorer un graphe à l'aide de branch and bound.
    * g : le graphe à colorer.
    * return_on_first_leaf : un indicateur pour retourner lors de l'atteinte de la première solution.
    * recursive : un indicateur pour utiliser l'implémentation récursive ou itérative de branch and bound.
    """
    print(f"Number of vertices: {g.num_vertices}, number of edges: {g.num_edges}")

    # Démarrer le chrono
    start_time = time.time()

    if recursive:
        # Appelez l'implémentation récursive.
        branch_and_bound_recursive(g, return_on_first_leaf)
    else:
        # Appeler l'implémentation itérative.
        branch_and_bound_iterative(g, return_on_first_leaf)

    # Arrêter le chrono.
    end_time = time.time()

    # Afficher les résultats.
    print("optimum number of colors: ", g.optimum)
    print("coloring: ", g.colors)
    print("Execution time: ", end_time - start_time)

    return g.optimum, end_time - start_time
