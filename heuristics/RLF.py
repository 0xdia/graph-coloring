def rlf(g):
    def choose_next(not_adjacent_to_colored, adjacent_to_colored):
        return sorted(
            [
                (len(get_neighbors_in_subgraph(v, adjacent_to_colored)), v)
                for v in not_adjacent_to_colored
            ]
        )[-1][1]

    def get_neighbors_in_subgraph(x, X):
        return [v for v in g.get_neighbors(x) if v in X]

    def vertex_of_max_degree_in_subgraph(X):
        return sorted([(len(get_neighbors_in_subgraph(v, X)), v) for v in X])[-1][1]

    def recurse(X, current_color):
        g.optimum = current_color + 1
        # S = set()
        x = vertex_of_max_degree_in_subgraph(X)
        # print(f"set color of {x} to {current_color}")
        g.colors[x] = current_color
        # S.add(x)

        adjacent_to_colored = set(get_neighbors_in_subgraph(x, X))
        X.remove(x)
        not_adjacent_to_colored = set([v for v in X if v not in adjacent_to_colored])

        while len(not_adjacent_to_colored) != 0:
            x = choose_next(not_adjacent_to_colored, adjacent_to_colored)
            g.colors[x] = current_color
            # S.add(x)
            not_adjacent_to_colored.remove(x)
            x_neighbors = get_neighbors_in_subgraph(x, X)
            # print(f"set color of {x} to {current_color}")
            # print("its neighbors are ", x_neighbors)
            # print("X is ", X)
            for n in x_neighbors:
                # S.add(n)
                if n in not_adjacent_to_colored:
                    not_adjacent_to_colored.remove(n)
                adjacent_to_colored.add(n)

            X.remove(x)

        # print("adjacent to colored: ", adjacent_to_colored)
        if len(adjacent_to_colored) != 0:
            recurse(adjacent_to_colored.copy(), current_color + 1)

    X = set([i for i in range(g.num_vertices)])

    # print('get neighbors in sub: ', get_neighbors_in_subgraph(0, X))
    # print('vertex of max deg: ', vertex_of_max_degree_in_subgraph(X))
    # return

    g.optimum = current_color = 0
    recurse(X, current_color)
