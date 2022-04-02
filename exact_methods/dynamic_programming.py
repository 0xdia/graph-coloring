import time


def dp_solve(g):
    """
    Solves graph coloring problem using dynamic programming.
    * g : le graphe à colorer.
    """
    # Create a list to hold the independent sets.
    independent_sets = []

    # Create a list to hold the color for each independent set.
    sets_colors = []

    # No colors used yet.
    current_color = -1

    for vertex in range(g.num_vertices):
        added = False

        # Find the maximum independent set for this vertex.
        for i in range(len(independent_sets)):

            # Check if this vertex can be added to this independent set.
            if g.is_independent_set(vertex, independent_sets[i]):
                independent_sets[i].add(vertex)

                # mark as added to an independent set.
                added = True

                # set the color of the vertex to the color of the independent set it belongs to
                g.colors[vertex] = sets_colors[i]
                for j in range(i, 0, -1):
                    # Reorder the independent sets
                    # To always populate the longest independent set first
                    # (to find the maximum independent set for the vertex)
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

        # Create a new independent set and a new color for it
        # and add this vertex to it.
        if not added:
            current_color += 1
            g.colors[vertex] = current_color
            independent_sets.append(set([vertex]))
            sets_colors.append(current_color)

    g.optimum = current_color + 1


def measured_dp(g):
    """
    Measure the time it takes to color a graph using dynamic programming.
    * g: the graph to be colored.
    """
    print(f"Number of vertices: {g.num_vertices}, number of edges: {g.num_edges}")

    start_time = time.time()
    dp_solve(g)
    end_time = time.time()

    print("optimum number of colors: ", g.optimum)
    print("coloring: ", g.colors)
    print("Execution time: ", end_time - start_time)
