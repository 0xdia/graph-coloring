import time
from random import seed, uniform

seed(time.time())


def individual_dies(g, individual):
    g.colors = individual
    return not g.validate_solution()


def roulette(population, percentage):
    pool = []
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
    return pool


def elitist(population):
    pass


def tournament(population):
    pass


def ranking(population):
    pass


def random(population):
    pass
