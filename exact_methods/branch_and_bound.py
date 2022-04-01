import heapq
import time

recursion_depth = 0


def branch_and_bound_recursive(g, return_on_first_leaf=False):
    def search(g, sub_coloring, num_colors, num_non_colored):
        global recursion_depth
        recursion_depth += 1
        if return_on_first_leaf and g.optimum < g.num_vertices + 1:
            return

        if num_non_colored == 0 and num_colors < g.optimum:
            g.optimum = num_colors
            g.colors = sub_coloring.copy()
            return

        if num_colors >= g.optimum:
            return

        new_color = num_colors
        extended_sub_coloring = []

        for i in range(len(sub_coloring)):
            # when sub_coloring[i] != -1, setting possibility and not_yet_colored 
            # was a waste of time because of the continue commande
            # so i delayed it until the first i for which sub_coloring[i] == -1
            if sub_coloring[i] != -1:
                continue
            not_yet_colored = num_non_colored
            possibility = sub_coloring.copy()

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
    # we don't initialize optimum to num_vertices
    # because later if the actual required number of colors is
    # num_vertices, the solution will never be updated.
    g.optimum = g.num_vertices + 1
    search(g, sub_coloring, 0, g.num_vertices)
    print("recursion_depth is; ", recursion_depth)


def branch_and_bound_iterative(g, return_on_first_leaf=False):
    # we don't initialize optimum to num_vertices
    # because later if the actual required number of colors is
    # num_vertices, the solution will never be updated.
    g.optimum = g.num_vertices + 1
    pq = []
    heapq.heappush(pq, (g.num_vertices, 0, [-1 for _ in range(g.num_vertices)]))
    while len(pq) != 0:
        num_non_colored, num_colors, sub_coloring = heapq.heappop(pq)
        if return_on_first_leaf and g.optimum < g.num_vertices + 1:
            break

        if num_non_colored == 0 and num_colors < g.optimum:
            g.optimum = num_colors
            g.colors = sub_coloring.copy()
            continue

        new_color = num_colors
        for i in range(len(sub_coloring)):
            # when sub_coloring[i] != -1, setting possibility and not_yet_colored 
            # was a waste of time because of the continue commande
            # so i delayed it until the first i for which sub_coloring[i] == -1
            if sub_coloring[i] != -1:
                continue
            not_yet_colored = num_non_colored
            possibility = sub_coloring.copy()

            possibility[i] = new_color
            not_yet_colored -= 1
            for j in range(len(possibility)):
                if possibility[j] != -1:
                    continue
                neighbors_colors = g.get_neighbors_colors(j, possibility)
                if new_color not in neighbors_colors:
                    possibility[j] = new_color
                    not_yet_colored -= 1

            if new_color + 1 >= g.optimum:
                continue

            if not (not_yet_colored, new_color + 1, possibility) in pq:
                heapq.heappush(pq, (not_yet_colored, new_color + 1, possibility))

    return


def measured_branch_and_bound(g, return_on_first_leaf=False, recursive=False):
    print(f"Number of vertices: {g.num_vertices}, number of edges: {g.num_edges}")
    start_time = end_time = None
    if recursive:
        start_time = time.time()
        branch_and_bound_recursive(g, return_on_first_leaf)
        end_time = time.time()
    else:
        start_time = time.time()
        branch_and_bound_iterative(g, return_on_first_leaf)
        end_time = time.time()
    print("optimum number of colors: ", g.optimum)
    print("coloring: ", g.colors)
    print("Execution time: ", end_time - start_time)
