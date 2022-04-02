import time


def dp_solve(g):
    independent_sets = []
    sets_colors = []
    current_color = -1

    for vertex in range(g.num_vertices):
        added = False
        for i in range(len(independent_sets)):
            if g.is_independent_set(vertex, independent_sets[i]):
                independent_sets[i].add(vertex)
                added = True
                g.colors[vertex] = sets_colors[i]
                for j in range(i, 0, -1):
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

        if not added:
            current_color += 1
            g.colors[vertex] = current_color
            independent_sets.append(set([vertex]))
            sets_colors.append(current_color)

    g.optimum = current_color + 1


def measured_dp(g):
    start_time = time.time()
    dp_solve(g)
    end_time = time.time()
    print("Execution time: ", end_time - start_time)
