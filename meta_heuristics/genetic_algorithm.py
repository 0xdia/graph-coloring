import time

from .genetic_algo_steps.crossing import crossing_in_pool
from .genetic_algo_steps.initialize_population import init_population
from .genetic_algo_steps.mutation import mutation_in_pool
from .genetic_algo_steps.selection import selection
from .genetic_algo_steps.replacement import replacement


def genetic_algorithm(
    g,
    pool_size,
    selection_strategy,
    selection_percentage,
    crossing_proba,
    num_of_matings=1,
    crossing_manner="1",
    mutation_proba=0.5,
    nbr_iterations=100,
):

    population = init_population(g, pool_size)

    for _ in range(nbr_iterations + 1):
        print(f"[*] Generation {_}")
        # print(f"[*] Generation {_}, Population size = {len(population)}")
        if len(population) == 1:
            break
        population = selection(
            population, pool_size, selection_strategy, selection_percentage
        )
        print(f"After selection: {len(population)}")
        new = crossing_in_pool(
            g, population, crossing_proba, num_of_matings, crossing_manner
        )
        print(f"After crossing: {len(new)}")
        new = mutation_in_pool(g, new, mutation_proba)
        print(f"After mutation: {len(new)}")
        new = replacement(new, pool_size)
        print(f"After replacement: {len(new)}")
        population = new.copy()


def measure_genetic_algorithm(
    g,
    pool_size,
    selection_strategy,
    selection_percentage,
    crossing_proba,
    num_of_matings=1,
    crossing_manner="uniform",
    mutation_proba=0.5,
    nbr_iterations=100,
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
    g.validate_solution()
    print("==== solution ====")
    print("Number of vertices: ", g.num_vertices)
    print("Number of colors: ", g.optimum)
    print("Colors: ", g.colors)
    print("Execution time: ", end_time - start_time)
