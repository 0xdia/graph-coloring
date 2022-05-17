from random import randint, seed, uniform
from time import time

seed(time())  # initialize the seed


def selection(population, strategy="random", percentage=0.5):
    assert 0.0 < percentage and percentage < 1.0 
    pool = []

    def roulette():
        unique_colors = [len(set(individual)) for individual in population]
        n = sum(unique_colors)
        pop_size = len(population)
        sectors = [
            ((n - num_colors) * 360 / float(n * (pop_size - 1)))
            for num_colors in unique_colors
        ]

        for i in range(1, len(sectors)):
            sectors[i] += sectors[i - 1]

        selected = [False for _ in range(len(population))]
        while len(pool) < int(pop_size * percentage):
            random_deg = uniform(0.0, 359.99)
            for i in range(0, len(sectors)):
                if random_deg <= sectors[i]:
                    if selected[i]:
                        break
                    pool.append(population[i])
                    selected[i] = True
                    break

    def elitist():
        pass

    def tournament():
        pass

    def ranking():
        pass

    def random():
        pass

    # this could be replaced with match-case introduced in python 3.10
    {
        "roulette": roulette(),
        "elitist": elitist(),
        "tournament": tournament(),
        "ranking": ranking(),
        "random": random(),
    }[strategy]

    return pool


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


a = [1, 2, 3, 4, 5, 5]
b = [10, 20, 30, 40, 50, 60]
c = [0, 4, 5, 6, 0, 0]
d = [2, 5, 6, 7, 9, 7]

print(selection([a, b, c, d], "roulette"))
