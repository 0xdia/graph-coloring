from math import inf
import networkx as nx
import matplotlib.pyplot as plt


class graph:
    """
    Graph data structure
    """

    def __init__(self):
        self.adj_matrix = None
        self.adj_list = None
        self.edges = None
        self.num_vertices = 0
        self.num_edges = 0
        self.colors = None
        self.approximative_optimum = inf

    def read(self, input_file, mode):
        with open(input_file, "r") as f:
            input = f.read().strip().split("\n")

            self.approximative_optimum = self.num_vertices = int(input[0].split()[0])
            self.num_edges = int(input[0].split()[1])
            self.adj_matrix = [
                [0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)
            ]
            self.adj_list = [[] for _ in range(self.num_vertices)]
            self.edges = []
            self.colors = [-1 for _ in range(self.num_vertices)]

            if mode == "--adjlist":
                i = 0
                adj_list = input[1:]
                for lst in adj_list:
                    vertex, neighbors = int(lst.split()[0]), [
                        int(x) for x in lst.split()[1:]
                    ]
                    assert 0 <= vertex and vertex < self.num_vertices

                    # introducing a new row in the adjacency list
                    self.adj_list[vertex] = neighbors

                    # introducing a new row in the adjacency matrix and updating edges list
                    for neighbor in neighbors:
                        self.adj_matrix[vertex][neighbor] = 1
                        if (neighbor, vertex) not in self.edges:
                            self.edges.append((vertex, neighbor))
            else:
                edges = input[1:]
                assert len(edges) == self.num_edges

                for edge in edges:
                    edge = [int(x) for x in edge.split()]
                    assert len(edge) == 2
                    assert 0 <= edge[0] and edge[0] < self.num_vertices
                    assert 0 <= edge[0] and edge[0] < self.num_vertices

                    # append each vertex of the edge as neighbor to the other
                    self.adj_list[edge[0]].append(edge[1])
                    self.adj_list[edge[1]].append(edge[0])

                    # set the neighborhood in the adjacency matrix
                    self.adj_matrix[edge[0]][edge[1]] = 1
                    self.adj_matrix[edge[1]][edge[0]] = 1

                    # update edges list
                    self.edges.append(edge)

    def get_neighbors(self, vertex):
        assert vertex < self.num_vertices
        return self.adj_list[vertex]

    def get_neighbors_colors(self, vertex, sub_coloring):
        neighbors = self.get_neighbors(vertex)
        neighbors_colors = [sub_coloring[i] for i in neighbors if sub_coloring[i] != -1]
        return neighbors_colors

    def visualize_graph(self):
        G = nx.Graph()
        G.add_nodes_from([i for i in range(self.num_vertices)])
        G.add_edges_from(self.edges)
        nx.draw_networkx(G, node_color=self.colors)
        plt.show()
