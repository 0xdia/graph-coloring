from math import inf
import networkx as nx
import matplotlib.pyplot as plt


class graph:
    """
    Graph data structure
    """

    def __init__(self):
        self.adj_matrix = None  # Adjacency matrix data structure.
        self.adj_list = None  # Adjacency list data structure.
        self.edges = None  # List of edges data structure.
        self.num_vertices = 0  # The number of vertices in the graph.
        self.num_edges = 0  # The number of vertices in the graph.
        self.colors = None  # The colors of the verticies of g.
        self.optimum = inf  # The optimum number of colors used to color the graph.

    def read(self, input_file, mode, indexation):
        """
        Read an input file and populate the graph
        * self: the graph object.
        * input_file: the file to read from.
        * mode: an option to indicate the reading mode,
            could be "--adjlist" or "--adjmatrix".
        * indexation: an option to indicate the starting index of the graph,
            could be "--0-indexed" or "--1-indexed".
        """
        with open(input_file, "r") as f:
            input = f.read().strip().split("\n")

            # The first line of the file gives us the number of vertices
            # and the number of edges.
            self.num_vertices = int(input[0].split()[0])
            self.num_edges = int(input[0].split()[1])

            # Initialize the graph data structures.
            self.adj_matrix = [
                [0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)
            ]
            self.adj_list = [[] for _ in range(self.num_vertices)]
            self.edges = []

            # initialize the colors of verticies to -1 (not colored).
            self.colors = [-1 for _ in range(self.num_vertices)]

            if mode == "--adjlist":
                adj_list = input[1:]

                # For each line in the input file get the vertex and its adjacency list.
                for lst in adj_list:
                    vertex, neighbors = int(lst.split()[0]), [
                        int(x) for x in lst.split()[1:]
                    ]

                    # Consider indexation.
                    if indexation == "--1-indexed":
                        vertex -= 1

                    # Check the integrity of the data.
                    assert 0 <= vertex and vertex < self.num_vertices

                    # introduce a new list in the adjacency list.
                    self.adj_list[vertex] = neighbors

                    # introduce a new row in the adjacency matrix and update edges list.
                    for neighbor in neighbors:
                        self.adj_matrix[vertex][neighbor] = 1
                        if (neighbor, vertex) not in self.edges:
                            self.edges.append((vertex, neighbor))
            else:
                edges = input[1:]

                # Check the integrity of the data.
                assert len(edges) == self.num_edges

                # For each line in the input file get an edge.
                for edge in edges:
                    edge = [int(x) for x in edge.split()]
                    assert len(edge) == 2

                    # Consider indexation.
                    if indexation == "--1-indexed":
                        edge[0] -= 1
                        edge[1] -= 1

                    # Check the integrity of the data.
                    assert 0 <= edge[0] and edge[0] < self.num_vertices
                    assert 0 <= edge[1] and edge[1] < self.num_vertices

                    # Append each vertex of the edge as neighbor to the other.
                    self.adj_list[edge[0]].append(edge[1])
                    self.adj_list[edge[1]].append(edge[0])

                    # Set the neighborhood in the adjacency matrix.
                    self.adj_matrix[edge[0]][edge[1]] = 1
                    self.adj_matrix[edge[1]][edge[0]] = 1

                    # Update edges list.
                    self.edges.append(edge)

    def read(self, input_file):
        """
        Read an input file in DIMACS standard format and populate the graph
        * self: the graph object.
        * input_file: the file in DIMACS standard format to read from.
        """
        try:
            f = open(input_file, "r")

            # Read the file line by line.
            line = f.readline()

            # Read graph information and setting
            # the values of number of verticies, number of edges, and optimum.
            while line:
                if line[0] == "p":
                    splited_line = line.split(" ")
                    self.num_vertices = int(splited_line[2])
                    self.optimum = self.num_vertices + 1
                    self.num_edges = int(splited_line[3])
                    break
                line = f.readline()

            # Initialize the graph data structures.
            self.adj_matrix = [
                [0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)
            ]
            self.adj_list = [[] for _ in range(self.num_vertices)]
            self.edges = []

            # initialize the colors of verticies to -1 (not colored).
            self.colors = [-1 for _ in range(self.num_vertices)]

            # Read the edges.
            while line:
                if line[0] == "e":
                    line = line.replace("e ", "").split()
                    edge = [int(e) - 1 for e in line]

                    # Check the integrity of the data.
                    if not all(e < self.num_vertices for e in edge):
                        raise ValueError(
                            f"vertex number > number of vertices , Edge {edge[0]} {edge[1]}"
                        )
                        exit()
                    if len(edge) != 2:
                        raise ValueError(f"Invalide number of vertices {len(edge)}")
                        exit()

                    # Add the vertex to adjacency list.
                    self.adj_list[edge[0]].append(edge[1])
                    self.adj_list[edge[1]].append(edge[0])

                    # Add the vertex to adjacency matrix.
                    self.adj_matrix[edge[0]][edge[1]] = 1
                    self.adj_matrix[edge[1]][edge[0]] = 1

                    # Update edges list.
                    if (edge[1], edge[0]) not in self.edges:
                        self.edges.append((edge[0], edge[1]))
                line = f.readline()
            f.close()
        except FileNotFoundError:
            print("Wrong file or file path")
            exit()

    def get_neighbors(self, vertex):
        """
        Return the the neighbors of vertex.
        """
        assert vertex < self.num_vertices
        return self.adj_list[vertex]

    def get_neighbors_colors(self, vertex, sub_coloring):
        """
        Return the colors of the neighbors of vertex.
        """
        neighbors = self.get_neighbors(vertex)
        neighbors_colors = [sub_coloring[i] for i in neighbors if sub_coloring[i] != -1]
        return neighbors_colors

    def validate_solution(self):
        """
        Returns True if the coloring of the graph is valid.
        """
        for vertex in range(self.num_vertices):
            if self.colors[vertex] == -1:
                return False
            if self.colors[vertex] in self.get_neighbors_colors(vertex, self.colors):
                return False
        return True

    def is_independant_set(self, vertex, independant_set):
        """
        Returns True if { independant_set U {vertex} } is an independant set.
        """
        for element in independant_set:
            if self.adj_matrix[element][vertex]:
                return False
        return True

    def visualize_graph(self):
        """
        Visualize the colored graph
        """
        G = nx.Graph()
        G.add_nodes_from([i for i in range(self.num_vertices)])
        G.add_edges_from(self.edges)
        nx.draw_networkx(G, node_color=self.colors)
        plt.show()
