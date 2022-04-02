import time


def dp_solve(g):
    """
    Résout le problème de coloration des graphes à l'aide de la programmation dynamique.
    * g : le graphe à colorier. 
    """
    # Créez une liste pour contenir les ensembles indépendants.
    independent_sets = []
    
    # Créez une liste pour contenir la couleur de chaque ensemble indépendant.
    sets_colors = []
    
    # Pas encore de couleurs utilisées.
    current_color = -1

    for vertex in range(g.num_vertices):
        added = False

        # Trouvez l'ensemble indépendant maximal pour ce sommet. 
        for i in range(len(independent_sets)):

            # Vérifiez si ce sommet peut être ajouté à cet ensemble indépendant. 
            if g.is_independent_sets(vertex, independent_sets[i]):
                independent_sets[i].add(vertex)

                # Marquer ce sommet comme ajouté à un ensemble indépendant. 
                added = True

                # colorer le sommet par la couleur de l'ensemble indépendant auquel il appartient 
                g.colors[vertex] = sets_colors[i]
                for j in range(i, 0, -1):
                    # Réorganisez les ensembles indépendants
                    # pour toujours remplir d'abord l'ensemble indépendant le plus long.
                    # (pour trouver l'ensemble indépendant maximum pour le sommet) 
                    if len(independent_sets[j - 1]) < len(independent_sets[j]):
                        independent_sets[j - 1], independent_sets[j] = (
                            independent_sets[j],
                            independent_sets[j - 1],
                        )
                        sets_colors[j - 1], sets_colors[j] = (
                            sets_colors[j],
                            sets_colors[j - 1],
                        )
                    else:
                        break
                break
        
        # Créez un nouvel ensemble indépendant
        # et une nouvelle couleur pour celui-ci et ajoutez-lui ce sommet. 
        if not added:
            current_color += 1
            g.colors[vertex] = current_color
            independent_sets.append(set([vertex]))
            sets_colors.append(current_color)

    g.optimum = current_color + 1


def measured_dp(g):
    """
    Mesurez le temps nécessaire pour colorer un graphe à l'aide de la programmation dynamique.
    * g : le graphe à colorier. 
    """
    print(f"Number of vertices: {g.num_vertices}, number of edges: {g.num_edges}")

    start_time = time.time()
    dp_solve(g)
    end_time = time.time()

    print("optimum number of colors: ", g.optimum)
    print("coloring: ", g.colors)
    print("Execution time: ", end_time - start_time)
