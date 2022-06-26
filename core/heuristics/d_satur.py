import time


def d_satur(g):
    """
    Implementation of the DSatur heuristic to solve the coloring problem of a graph.
        * g : the graph to be colored
    """

    def next_vertex(uncolored_vertices):
        """
        Returns the next vertex to be colored.
        * uncolored_vertices : dictionary where (key, value) = (uncolored_vertex, [degree_of_saturation, degree_in_uncolored_subgraph])
        """
        # Sort the dictionary using values
        # and return the uncolored vertex with the highest degree of saturation.
        # In cases of ties, cosider the largest degree in the subgraph induced by the uncolored vertices as a second attribute.
        return sorted(uncolored_vertices, key=uncolored_vertices.get)[-1]

    def color(g, vertex):
        """
        Colors the vertex.
        * g : the graph to be colored
        * vertex: the vertex to be colored
        """
        vertex_color = 0
        neighbors_colors = g.get_neighbors_colors(vertex, g.colors)
        if neighbors_colors:
            # Find the lowest color not being used by any of the neighbors.
            # `vertex_color` could be a color in range (0,max(neighbors_colors)) or max(neighbors_colors)+1
            for vertex_color in range(max(neighbors_colors) + 2):
                if vertex_color not in neighbors_colors:
                    break
        g.colors[vertex] = vertex_color

    def is_color_in_neighbors(g, vertex, color):
        """
        Check if any neighbors of `vertex` in `g` is colored with `color`.
        * g : the graph to be colored
        * vertex: the vertex whose neighbors are going to be checked
        * color: the color to be checked
        """
        return color in g.get_neighbors_colors(vertex, g.colors)

    # initialization
    # dictionary where (key, value) = (uncolored_vertex, [degree_of_saturation, degree_in_uncolored_subgraph])
    uncolored_vertices = {}
    for vertex in range(g.num_vertices):
        uncolored_vertices[vertex] = [0, g.degrees[vertex]]

    # while there are still uncolored vertices
    while len(uncolored_vertices) != 0:
        # get the next vertex to be colored
        vertex = next_vertex(uncolored_vertices)

        # color the vertex
        vertex_color = color(g, vertex)

        # update the dictionary
        for neighbor in g.get_neighbors(vertex):
            if g.colors[neighbor] == -1:
                # update the degree_in_uncolored_subgraph
                uncolored_vertices[neighbor][1] -= 1
                if not is_color_in_neighbors(g, neighbor, vertex_color):
                    # update the degree_of_saturation
                    uncolored_vertices[neighbor][0] += 1
        # remove the vertex (vertex is now colored)
        uncolored_vertices.pop(vertex)

    # update the optimum
    g.optimum = max(g.colors) + 1


def measure_d_satur(g):
    """
    Measure the time it takes to color a graph using DSatur heuristic.
    * g: the graph to be colored.
    """
    start_time = time.time()
    d_satur(g)
    end_time = time.time()

    print(f"Number of vertices: {g.num_vertices}, number of edges: {g.num_edges}")
    print("Optimum: ", g.optimum)
    print("Colors: ", g.colors)
    print("Execution time: ", end_time - start_time)
    return g.optimum ,  end_time - start_time