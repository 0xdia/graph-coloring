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


def individual_dies(g, individual):
    g.colors = individual
    return not g.validate_solution()


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


def crossing_in_pool(g, population, crossing_proba, num_of_matings, manner):
    num_crossings = int(len(population) * crossing_proba)
    print(num_crossings)
    new_population = population.copy()
    for _ in range(num_crossings):
        mother_idx = randint(0, len(population) - 1)
        father_idx = mother_idx
        while father_idx == mother_idx:
            father_idx = randint(0, len(population) - 1)

        for __ in range(num_of_matings):
            child_1, child_2 = crossing(
                population[father_idx], population[mother_idx], manner
            )

            if not individual_dies(g, child_1):
                new_population.append(child_1)
            if not individual_dies(g, child_2):
                new_population.append(child_2)

    return new_population


def mutation(individual):
    colors = list(set(individual))
    gene = randint(0, len(individual) - 1)
    new_gene = randint(0, len(colors) - 1)
    while colors[new_gene] == individual[gene]:
        new_gene = randint(0, len(colors) - 1)

    individual[gene] = colors[new_gene]


def genetic_algorithm(
    g,
    initial_population_size,
    selection_strategy,
    selection_percentage,
    crossing_proba,
    num_of_matings,
    crossing_manner,
    mutation_proba,
    nbr_iterations,
):
    # For instance, we intialize the population randomly
    population = [
        [randint(0, g.num_vertices) for i in range(g.num_vertices)]
        for _ in range(initial_population_size)
    ]

    for iter in range(nbr_iterations):
        print("size of pop before selection = ", len(population))
        population = selection(population, selection_strategy, selection_percentage)
        print("size of pop after selection = ", len(population))
        new = crossing_in_pool(
            g, population, crossing_proba, num_of_matings, crossing_manner
        )
        print("size of pop after crossing = ", len(new))
        break
