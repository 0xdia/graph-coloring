import heapq
import time

recursion_depth = 0


def branch_and_bound_recursive(g, return_on_first_leaf=False):
    """
    Recursive implimentation of branch and bound algorithm to
    solve the coloring problem in a graph.
    * g: the graph to be colored
    * return_on_first_leaf: a flag to return when reaching the first solution.
    """

    def search(g, sub_coloring, num_colors, num_non_colored):
        """
        Recursive function to evaluate an internal node in the branch and bound tree.
        * g: the graph to be colored.
        * sub_coloring : the internal node.
        * num_colors: nombre of colors used in this node.
        * num_non_colored: nomber of uncolored vertices in this node.
        """
        # Keep track of how many times `search` is executed.
        global recursion_depth
        recursion_depth += 1

        # Return if the optimum was updated and the `return_on_first_leaf` flag is true.
        if return_on_first_leaf and g.optimum < g.num_vertices + 1:
            return

        # Update the optimal number of colors and the colors of the vertices of g 
        # if a better solution is found.
        if num_non_colored == 0 and num_colors < g.optimum:
            g.optimum = num_colors
            g.colors = sub_coloring.copy()
            return

        # Cut the branch if the number of colors used so far
        # is already bigger than or equal the optimum.
        if num_colors >= g.optimum:
            return

        # Introduce a new color.
        new_color = num_colors

        # Create list to hold children of this node.
        extended_sub_coloring = []

        # Create children for this node.
        for i in range(len(sub_coloring)):
            # Find the next uncolored vertex.
            if sub_coloring[i] != -1:
                continue

            # Initialize a new child.
            not_yet_colored = num_non_colored
            possibility = sub_coloring.copy()

            # Color the uncolored vertex found with the new color.
            possibility[i] = new_color
            not_yet_colored -= 1

            # Color as much verticies as possible with the new color.
            for j in range(len(possibility)):
                # Find the next uncolored vertex.
                if possibility[j] != -1:
                    continue

                # Color the uncolored vertex found with the new color
                # if there's no conflict with neighbors colors.
                neighbors_colors = g.get_neighbors_colors(j, possibility)
                if new_color not in neighbors_colors:
                    possibility[j] = new_color
                    not_yet_colored -= 1

            # Add the new child to the list.
            if (not_yet_colored, possibility) not in extended_sub_coloring:
                extended_sub_coloring.append((not_yet_colored, possibility))

        # Sort the children in ascending order based on
        # the value of not_yet_colored (closest to leaf).
        extended_sub_coloring.sort()

        # Call `search` on each child created.
        for extended in extended_sub_coloring:
            search(g, extended[1], new_color + 1, extended[0])

    # Initalize the root node with no vertex colored.
    # Initalize the optimum with a value bigger than the worst case.
    sub_coloring = [-1 for _ in range(g.num_vertices)]
    g.optimum = g.num_vertices + 1

    # Start the search.
    search(g, sub_coloring, 0, g.num_vertices)
    print("recursion_depth is; ", recursion_depth)


def branch_and_bound_iterative(g, return_on_first_leaf=False):
    """
    Iterative implimentation of branch and bound algorithm
    to solve the coloring problem in a graph
    * g: the graph to be colored
    * return_on_first_leaf: a flag to return when reaching the first solution.
    """
    # Initalize the optimum with a value bigger than the worst case.
    g.optimum = g.num_vertices + 1

    # Create a priority queue to hold nodes
    # with nodes closest to leaf (having the least number of uncolored verticies),
    # and using less colors, in that order
    # having a higher priority.
    pq = []

    # Push the root node to the queue
    heapq.heappush(pq, (g.num_vertices, 0, [-1 for _ in range(g.num_vertices)]))

    # While not all branches were evaluated
    while len(pq) != 0:

        # Pop the highest priority node
        num_non_colored, num_colors, sub_coloring = heapq.heappop(pq)

        # Return if the optimum was updated and the `return_on_first_leaf` flag is true.
        if return_on_first_leaf and g.optimum < g.num_vertices + 1:
            break

        # Update the optimum number of colors and the colors of the verticies of g
        # if a better solution is found.
        if num_non_colored == 0 and num_colors < g.optimum:
            g.optimum = num_colors
            g.colors = sub_coloring.copy()
            continue

        # Inroduce a new color.
        new_color = num_colors

        # Create children for this node.
        for i in range(len(sub_coloring)):
            # Find the next uncolored vertex.
            if sub_coloring[i] != -1:
                continue

            # Initialize a new child.
            not_yet_colored = num_non_colored
            possibility = sub_coloring.copy()

            # Color the uncolored vertex found with the new color.
            possibility[i] = new_color
            not_yet_colored -= 1

            # Color as much verticies as possible with the new color.
            for j in range(len(possibility)):
                # Find the next uncolored vertex.
                if possibility[j] != -1:
                    continue

                # Color the uncolored vertex found with the new color
                # if there's no conflict with neighbors.
                neighbors_colors = g.get_neighbors_colors(j, possibility)
                if new_color not in neighbors_colors:
                    possibility[j] = new_color
                    not_yet_colored -= 1

            # Cut the branch if the number of colors used so far
            # is already bigger than or equal the optimum.
            if new_color + 1 >= g.optimum:
                continue

            # Add the new child to the queue.
            if not (not_yet_colored, new_color + 1, possibility) in pq:
                heapq.heappush(pq, (not_yet_colored, new_color + 1, possibility))

    return


def measured_branch_and_bound(g, return_on_first_leaf=False, recursive=False):
    """
    Measure the time it takes to color a graph using branch and bound.
    * g: the graph to be colored.
    * return_on_first_leaf: a flag to return when reaching the first solution.
    * recursive : a flag to use recursive or iterative implimentation of branch and bound.
    """
    print(f"Number of vertices: {g.num_vertices}, number of edges: {g.num_edges}")

    # Start timer
    start_time = time.time()

    if recursive:
        # Call the recursive implimentaion
        branch_and_bound_recursive(g, return_on_first_leaf)
    else:
        # Call the iterative implimentaion
        branch_and_bound_iterative(g, return_on_first_leaf)

    # Stop timer
    end_time = time.time()

    # Print results
    print("optimum number of colors: ", g.optimum)
    print("coloring: ", g.colors)
    print("Execution time: ", end_time - start_time)