from random import randint, seed
from time import time

seed(time())  # initialize the seed


def crossing(father, mother, manner="1"):
    def uniform_crossing(father, mother):
        first_child, second_child = father.copy(), mother.copy()
        for i in range(len(father)):
            if randint(0, 1) == 1:
                first_child[i], second_child[i] = second_child[i], first_child[i]
        return first_child, second_child

    def k_points_crossing(father, mother, k):
        # to avoid infinite loop when looking for random points
        assert k <= len(father) - 1

        segments = [0, len(father)]
        while len(segments) < k + 2:
            random_point = randint(1, len(father) - 1)
            if random_point not in segments:
                segments.append(random_point)
        segments.sort()

        first_child, second_child = father.copy(), mother.copy()
        cross = False
        for i in range(len(segments) - 1):
            if cross:
                (
                    first_child[segments[i] : segments[i + 1]],
                    second_child[segments[i] : segments[i + 1]],
                ) = (
                    second_child[segments[i] : segments[i + 1]],
                    first_child[segments[i] : segments[i + 1]],
                )
            cross = not cross
        return first_child, second_child

    assert len(father) == len(mother)
    return (
        uniform_crossing(father, mother)
        if manner == "uniforme"
        else k_points_crossing(father, mother, int(manner))
    )


def mutation(individual):
    colors = list(set(individual))
    gene = randint(0, len(individual) - 1)
    new_gene = randint(0, len(colors) - 1)
    while colors[new_gene] == individual[gene]:
        new_gene = randint(0, len(colors) - 1)

    individual[gene] = colors[new_gene]


father = [1, 2, 3, 4, 5, 5]
mother = [10, 20, 30, 40, 50, 60]

mutation(father)

print(father)
