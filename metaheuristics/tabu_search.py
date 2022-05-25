from collections import deque
from random import randrange
from heuristics.d_satur import d_satur
import time


def tabucol(graph, tabu_size=7, reps=100, max_iterations=10000, debug=False):
    # graph is assumed to be the adjacency matrix of an undirected graph with no self-loops
    # nodes are represented with indices, [0, 1, ..., n-1]
    # colors are represented by numbers, [0, 1, ..., k-1]
    d_satur(graph)
    colors = list(range(graph.optimum))
    # number of iterations of the tabucol algorithm
    iterations = 0
    # initialize tabu as empty queue
    tabu = deque()

    # solution is a map of nodes to colors
    # Generate a random solution:
    solution = []
    for i in range(graph.num_vertices):
        solution.append(colors[randrange(0, len(colors))])

    # Aspiration level A(z), represented by a mapping: f(s) -> best f(s') seen so far
    aspiration_level = dict()

    while iterations < max_iterations:
        # Count node pairs (i,j) which are adjacent and have the same color.
        move_candidates = set()  # use a set to avoid duplicates
        conflict_count = 0
        for i in range(graph.num_vertices):
            for j in range(
                i + 1, graph.num_vertices
            ):  # assume undirected graph, ignoring self-loops
                if graph.adj_matrix[i][j] > 0:  # adjacent
                    if solution[i] == solution[j]:  # same color
                        move_candidates.add(i)
                        move_candidates.add(j)
                        conflict_count += 1
        move_candidates = list(move_candidates)  # convert to list for array indexing

        if conflict_count == 0:
            # Found a valid coloring.
            break

        # Generate neighbor solutions.
        new_solution = None
        for r in range(reps):
            # Choose a node to move.
            node = move_candidates[randrange(0, len(move_candidates))]

            # Choose color other than current.
            new_color = colors[randrange(0, len(colors) - 1)]
            if solution[node] == new_color:
                # essentially swapping last color with current color for this calculation
                new_color = colors[-1]

            # Create a neighbor solution
            new_solution = solution.copy()
            new_solution[node] = new_color
            # Count adjacent pairs with the same color in the new solution.
            new_conflicts = 0
            for i in range(graph.num_vertices):
                for j in range(i + 1, graph.num_vertices):
                    if (
                        graph.adj_matrix[i][j] > 0
                        and new_solution[i] == new_solution[j]
                    ):
                        new_conflicts += 1
            if new_conflicts < conflict_count:  # found an improved solution
                # if f(s') <= A(f(s)) [where A(z) defaults to z - 1]
                if new_conflicts <= aspiration_level.setdefault(
                    conflict_count, conflict_count - 1
                ):
                    # set A(f(s) = f(s') - 1
                    aspiration_level[conflict_count] = new_conflicts - 1

                    if (
                        node,
                        new_color,
                    ) in tabu:  # permit tabu move if it is better any prior
                        tabu.remove((node, new_color))
                        if debug:
                            print(
                                "tabu permitted;", conflict_count, "->", new_conflicts
                            )
                        break
                else:
                    if (node, new_color) in tabu:
                        # tabu move isn't good enough
                        continue
                if debug:
                    print(conflict_count, "->", new_conflicts)
                break

        # At this point, either found a better solution,
        # or ran out of reps, using the last solution generated

        # The current node color will become tabu.
        # add to the end of the tabu queue
        tabu.append((node, solution[node]))
        if len(tabu) > tabu_size:  # queue full
            tabu.popleft()  # remove the oldest move

        # Move to next iteration of tabucol with new solution
        solution = new_solution
        iterations += 1
        if debug and iterations % 500 == 0:
            print("iteration:", iterations)

    # print("Aspiration Levels:\n" + "\n".join([str((k,v)) for k,v in aspiration_level.items() if k-v > 1]))

    # At this point, either conflict_count is 0 and a coloring was found,
    # or ran out of iterations with no valid coloring.
    if conflict_count != 0:
        print("No coloring found with {} colors.".format(graph.num_vertices))
        return None
    else:
        graph.colors = solution.copy()
        graph.optimum = len(set(solution))


def measure_tabu(g, tabu_size=7, reps=100, max_iterations=10000, debug=False):
    """
    Measure the time it takes to color a graph using DSatur heuristic.
    * g: the graph to be colored.
    """
    start_time = time.time()
    tabucol(g, tabu_size, reps, max_iterations, debug)
    end_time = time.time()

    print(f"Number of vertices: {g.num_vertices}, number of edges: {g.num_edges}")
    print("Optimum: ", g.optimum)
    print("Colors: ", g.colors)
    print("Execution time: ", end_time - start_time)
