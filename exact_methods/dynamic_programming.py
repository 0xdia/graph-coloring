import time


def dp_solve(g):
    independant_sets = []
    sets_colors = []
    current_color = -1

    for vertex in range(g.num_vertices):
        added = False
        for i in range(len(independant_sets)):
            if g.is_independant_set(vertex, independant_sets[i]):
                independant_sets[i].add(vertex)
                added = True
                g.colors[vertex] = sets_colors[i]
                for j in range(i, 0, -1):
                    if len(independant_sets[j - 1]) < len(independant_sets[j]):
                        independant_sets[j - 1], independant_sets[j] = (
                            independant_sets[j],
                            independant_sets[j - 1],
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
            independant_sets.append(set([vertex]))
            sets_colors.append(current_color)

    g.approximative_optimum = current_color + 1


def measure_execution_time(g):
    start_time = time.time()
    dp_solve(g)
    end_time = time.time()
    print("Execution time: ", end_time - start_time)
