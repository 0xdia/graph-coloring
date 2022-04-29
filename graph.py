from math import inf
import networkx as nx
import matplotlib.pyplot as plt


class graph:
    """
    Structure des données du graphe
    """

    def __init__(self):
        self.adj_matrix = None  # Matrice d'adjacence.
        self.adj_list = None  # Liste d'adjacence.
        self.edges = None  # Liste des arêtes.
        self.num_vertices = 0  # Le nombre de sommets dans le graphe.
        self.num_edges = 0  # Le nombre d'arêtes dans le graphe.
        self.colors = None  # Les couleurs des sommets de g.
        self.degrees = None
        self.optimum = (
            inf  # Le nombre optimal de couleurs utilisées pour colorer le graphe.
        )

    def read(self, input_file, mode, indexation):
        """
        Lire un fichier d'entrée et remplir le graph
        * self : l'objet graph.
        * input_file : le fichier à lire.
        * mode : une option pour indiquer le mode de lecture,
            peut être "--adjlist" ou "--adjmatrix".
        * indexation : une option pour indiquer l'indice de départ du graphe,
            peut être "--0-indexed" ou "--1-indexed".
        """
        with open(input_file, "r") as f:
            input = f.read().strip().split("\n")

            # La première ligne du fichier nous donne le nombre de sommets
            # et le nombre d'arêtes.
            self.num_vertices = int(input[0].split()[0])
            self.num_edges = int(input[0].split()[1])

            # Initialiser les structures de données du graphe.
            self.adj_matrix = [
                [0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)
            ]
            self.adj_list = [[] for _ in range(self.num_vertices)]
            self.edges = []

            # initialiser les couleurs des sommets à -1 (non coloré).
            self.colors = [-1 for _ in range(self.num_vertices)]

            self.degrees = [-1 for _ in range(self.num_vertices)]

            if mode == "--adjlist":
                adj_list = input[1:]

                # Pour chaque ligne du fichier d'entrée,
                # obtenir le sommet et sa liste d'adjacence.
                for lst in adj_list:
                    vertex, neighbors = (
                        int(lst.split()[0]),
                        [int(x) for x in lst.split()[1:]],
                    )

                    # Considérez l'indexation.
                    if indexation == "--1-indexed":
                        vertex -= 1

                    # Vérifier l'intégrité des données.
                    assert 0 <= vertex and vertex < self.num_vertices

                    # introduire une nouvelle liste dans la liste d'd'adjacence.
                    self.adj_list[vertex] = neighbors

                    self.degrees[vertex] = len(neighbors)

                    # introduire une nouvelle ligne dans la matrice d'adjacence
                    # et mettre à jour la liste des arêtes .
                    for neighbor in neighbors:
                        self.adj_matrix[vertex][neighbor] = 1
                        if (neighbor, vertex) not in self.edges:
                            self.edges.append((vertex, neighbor))
            else:
                edges = input[1:]

                # Vérifier l'intégrité des données.
                assert len(edges) == self.num_edges

                # Pour chaque ligne du fichier d'entrée, obtenez un arête.
                for edge in edges:
                    edge = [int(x) for x in edge.split()]
                    assert len(edge) == 2

                    # Considérez l'indexation.
                    if indexation == "--1-indexed":
                        edge[0] -= 1
                        edge[1] -= 1

                    # Vérifier l'intégrité des données.
                    assert 0 <= edge[0] and edge[0] < self.num_vertices
                    assert 0 <= edge[1] and edge[1] < self.num_vertices

                    # Ajouter chaque sommet de l'arête comme voisin de l'autre.
                    self.adj_list[edge[0]].append(edge[1])
                    self.adj_list[edge[1]].append(edge[0])

                    # Mettre le voisinage dans la matrice d'adjacence.
                    self.adj_matrix[edge[0]][edge[1]] = 1
                    self.adj_matrix[edge[1]][edge[0]] = 1

                    # Mettre à jour la liste des arêtes.
                    self.edges.append(edge)

                    self.degrees[edge[0]] += 1
                    self.degrees[edge[1]] += 1

    def read(self, input_file):
        """
        Lire un fichier d'entrée au format standard DIMACS et remplir le graphe.
        * self : l'objet graphe.
        * input_file : le fichier au format standard DIMACS à lire.
        """
        try:
            f = open(input_file, "r")

            # Lire le fichier ligne par ligne.
            line = f.readline()

            # Lire les informations du graphe
            # et définir les valeurs du nombre de sommets, du nombre d'arêtes et de l'optimum.
            while line:
                if line[0] == "p":
                    splited_line = line.split(" ")
                    self.num_vertices = int(splited_line[2])
                    self.optimum = self.num_vertices + 1
                    self.num_edges = int(splited_line[3])
                    break
                line = f.readline()

            # Initialiser les structures de données du graphe.
            self.adj_matrix = [
                [0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)
            ]
            self.adj_list = [[] for _ in range(self.num_vertices)]
            self.edges = []

            # initialise les couleurs des sommets à -1 (non coloré).
            self.colors = [-1 for _ in range(self.num_vertices)]

            self.degrees = [-1 for _ in range(self.num_vertices)]

            # Lire les arêtes du graphe.
            while line:
                if line[0] == "e":
                    line = line.replace("e ", "").split()
                    edge = [int(e) - 1 for e in line]

                    # Vérifiez l'intégrité des données.
                    if not all(e < self.num_vertices for e in edge):
                        raise ValueError(
                            f"vertex number > number of vertices , Edge {edge[0]} {edge[1]}"
                        )
                        exit()
                    if len(edge) != 2:
                        raise ValueError(f"Invalide number of vertices {len(edge)}")
                        exit()

                    # Ajouter le sommet à la liste d'adjacence.
                    self.adj_list[edge[0]].append(edge[1])
                    self.adj_list[edge[1]].append(edge[0])

                    # Mettre le voisinage dans la matrice d'adjacence.
                    self.adj_matrix[edge[0]][edge[1]] = 1
                    self.adj_matrix[edge[1]][edge[0]] = 1

                    # Mettre à jour la liste des arêtes.
                    if (edge[1], edge[0]) not in self.edges:
                        self.edges.append((edge[0], edge[1]))

                    self.degrees[edge[0]] += 1
                    self.degrees[edge[1]] += 1
                line = f.readline()
            f.close()
        except FileNotFoundError:
            print("Wrong file or file path")
            exit()

    def get_neighbors(self, vertex):
        """
        Retourner les voisins du sommet.
        """
        assert vertex < self.num_vertices
        return self.adj_list[vertex]

    def get_neighbors_colors(self, vertex, sub_coloring):
        """
        Retourner les couleurs des voisins du sommet.
        """
        neighbors = self.get_neighbors(vertex)
        neighbors_colors = [sub_coloring[i] for i in neighbors if sub_coloring[i] != -1]
        return neighbors_colors

    def validate_solution(self):
        """
        Retourner Vrai si la coloration du graphe est valide.
        """
        for vertex in range(self.num_vertices):
            if self.colors[vertex] == -1:
                return False
            if self.colors[vertex] in self.get_neighbors_colors(vertex, self.colors):
                return False
        return True

    def is_independent_set(self, vertex, independent_set):
        """
        Retourner Vrai si { independent_set U {vertex} } est un ensemble indépendant.
        """
        for element in independent_set:
            if self.adj_matrix[element][vertex]:
                return False
        return True

    def visualize_graph(self):
        """
        Visualiser le graphique coloré
        """
        G = nx.Graph()
        G.add_nodes_from([i for i in range(self.num_vertices)])
        G.add_edges_from(self.edges)
        nx.draw_networkx(G, node_color=self.colors)
        plt.show()
