from random import randint, seed, uniform
import time

seed(time.time())  # initialize the seed


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


def crossing_in_pool(g, pool_size, population, crossing_proba, num_of_matings, manner):
    new_population = population.copy()
    for i in range(len(population)):
        proba = uniform(0.0, 0.99)
        if proba > crossing_proba:
            continue

        for j in range(len(population)):
            proba = uniform(0.0, 0.99)
            if proba > crossing_proba or i == j:
                continue

            for _ in range(num_of_matings):
                child_1, child_2 = crossing(population[i], population[j], manner)

                if not individual_dies(g, child_1) and child_1 not in new_population:
                    new_population.append(child_1)
                if not individual_dies(g, child_2) and child_2 not in new_population:
                    new_population.append(child_2)

        if len(new_population) >= pool_size:
            break

    return new_population


def mutation(individual):
    colors = list(set(individual))
    gene = randint(0, len(individual) - 1)
    new_gene = randint(0, len(colors) - 1)
    while colors[new_gene] == individual[gene]:
        new_gene = randint(0, len(colors) - 1)

    individual[gene] = colors[new_gene]


def mutation_in_pool(g, population, mutation_proba):
    new = []
    for individual in population:
        proba = uniform(0.0, 0.99)
        if proba <= mutation_proba:
            mutation(individual)
        if not individual_dies(g, individual):
            new.append(individual)
            # check if individual is the best fitting to update the solution
            g.update_solution(individual)
    return new


def genetic_algorithm(
    g,
    pool_size,
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
        for _ in range(pool_size)
    ]

    for _ in range(nbr_iterations):
        if len(population) == 1:
            break

        population = selection(population, selection_strategy, selection_percentage)
        new = crossing_in_pool(
            g, pool_size, population, crossing_proba, num_of_matings, crossing_manner
        )
        new = mutation_in_pool(g, new, mutation_proba)
        population = new.copy()


def measure_genetic_algorithm(
    g,
    pool_size,
    selection_strategy,
    selection_percentage,
    crossing_proba,
    num_of_matings,
    crossing_manner,
    mutation_proba,
    nbr_iterations,
):
    start_time = time.time()
    genetic_algorithm(
        g,
        pool_size,
        selection_strategy,
        selection_percentage,
        crossing_proba,
        num_of_matings,
        crossing_manner,
        mutation_proba,
        nbr_iterations,
    )
    end_time = time.time()
    print("==== solution ====")
    print("Number of vertices: ", g.num_vertices)
    print("Number of colors: ", g.optimum)
    print("Colors: ", g.colors)
    print("Execution time: ", end_time - start_time)
