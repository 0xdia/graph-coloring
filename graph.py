
class graph:
    """
        Graph data structure
    """
    def __init__(self):
        self.adj_matrix = None
        self.adj_list   = None
        self.num_vertices = 0
        self.num_edges    = 0


    def read(self, input_file, mode):
        with open(input_file, 'r') as f:
            adj_list = f.read().strip().split('\n')

            self.num_vertices = int(adj_list[0].split()[0])
            self.num_edges    = int(adj_list[0].split()[1])
            self.adj_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
            self.adj_list   = [None for _ in range(self.num_vertices)]

            adj_list = adj_list[1:]
            for lst in adj_list:
                vertex, neighbors = int(lst.split()[0]), [int(x) for x in lst.split()[1:]]
                assert vertex < self.num_vertices
                
                # introducing a new row in the adjacency list
                self.adj_list[vertex] = neighbors

                # introducing a new row in the adjacency matrix
                for neighbor in neighbors:
                    self.adj_matrix[vertex][neighbor] = 1
