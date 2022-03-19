import time
from treelib import Node, Tree



def branch_and_bound(g):
    def search(g, sub_coloring, num_colors, num_non_colored,id,coloring_tree):
        if num_non_colored == 0 and num_colors < g.approximative_optimum:
            g.approximative_optimum = num_colors
            g.colors = sub_coloring.copy()
            return

        if num_colors >= g.approximative_optimum:
            return

        new_color = num_colors
        extended_sub_coloring = []

        ##########
        coloring_tree.append((id,sub_coloring))

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
            
            possibility_id = f'{id}.{i}'

            if (not_yet_colored, possibility) not in extended_sub_coloring:
                extended_sub_coloring.append((not_yet_colored, possibility,possibility_id))

        extended_sub_coloring.sort()
        for extended in extended_sub_coloring:
            search(g, extended[1], new_color + 1, extended[0],extended[2],coloring_tree)
    
    def display_tree(coloring_tree):
        coloring_tree.sort()
        tree = Tree()
        tree.create_node('n1','n1')
        for element in coloring_tree:
            print(f'Id={element[0]} : {element[1]}')    

    sub_coloring = [-1 for _ in range(g.num_vertices)]
    coloring_tree=[]
    search(g, sub_coloring, 0, g.num_vertices,str(0),coloring_tree)

def measure_execution_time(g):
    print(f"Number of vertices: {g.num_vertices}, number of edges: {g.num_edges}")
    start_time = time.time()
    branch_and_bound(g)
    end_time = time.time()
    print("optimum number of colors: ", g.approximative_optimum)
    print("coloring: ", g.colors)
    print("Execution time: ", end_time - start_time)


