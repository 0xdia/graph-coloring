import time
from random import randint, seed, uniform

from .helper_functions import individual_dies

seed(time.time())


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

    return new_population
