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
    crossing_manner="1",
    mutation_proba=0.5,
    nbr_iterations=100,
    param_tuning=False,
):

    population = init_population(g, pool_size)
    optimum_convergence = []
    if param_tuning:
        optimum_convergence.append(g.optimum)

    for _ in range(nbr_iterations-1):
        print(f"Generation = {_+1}")
        if len(population) == 1:
            break
        print(f"before selection, pop size = {len(population)}")
        population = selection(population, selection_strategy, selection_percentage)
        #print(f"before crossing, pop size = {len(population)}")
        crossing_in_pool(g, population, crossing_proba, crossing_manner)
        #print(f"before mutation, pop size = {len(population)}")
        new = mutation_in_pool(g, population, mutation_proba)
        #print(f"before replacement, pop size = {len(population)}")
        population = replacement(new, pool_size)
        # population = new.copy()

        if param_tuning:
            optimum_convergence.append(g.optimum)

    return optimum_convergence


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
