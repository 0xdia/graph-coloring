
def branch_and_bound(g):
    def search(g, sub_coloring, num_colors, num_non_colored):
        if num_non_colored == 0 and num_colors < g.approximative_optimum:
            g.approximative_optimum = num_colors
            g.colors = sub_coloring.copy()

        if num_colors >= g.approximative_optimum and num_non_colored > 0:
            return

        new_color = num_colors
        extended_sub_coloring = []

        for i in range(len(sub_coloring)):
            not_yet_colored = num_non_colored
            possibility = sub_coloring.copy()
            if possibility[i] != -1:
                continue

            possibility[i] = new_color
            not_yet_colored -= 1
            for j in range(len(possibility)):
                if possibility[j] != -1:
                    continue
                neighbors_colors = g.get_neighbors_colors(j, possibility)
                if new_color not in neighbors_colors:
                    possibility[j] = new_color
                    not_yet_colored -= 1

            if (not_yet_colored, possibility) not in extended_sub_coloring:
                extended_sub_coloring.append((not_yet_colored, possibility))

        extended_sub_coloring.sort()
        for extended in extended_sub_coloring:
            search(g, extended[1], new_color + 1, extended[0])

    sub_coloring = [-1 for _ in range(g.num_vertices)]
    search(g, sub_coloring, 0, g.num_vertices)
