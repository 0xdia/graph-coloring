import math
import matplotlib.pyplot as plt

import numpy as np
from .genetic_algorithm import genetic_algorithm
from time import time


def crossing_probability_impact(g, file_name):
    figure, axis = plt.subplots(1, 2)
    axis[0].set_title("Nombres des couleurs optimums")
    axis[0].legend(loc="best")
    axis[0].set_xlabel("Iterations")
    axis[0].set_ylabel("Optimal number of colors")
    axis[1].set_title("Temps d'execution")
    axis[1].legend(loc="best")
    axis[1].set_xlabel("Crossing probabilities")
    axis[1].set_ylabel("Temps d'execution")

    num_iterations = 50
    probabilities = [0.2, 0.4, 0.6, 0.8, 1.0]
    iterations = list(range(num_iterations))

    times = []
    min_optimum, max_optimum = g.num_vertices, 0
    for proba in probabilities:
        print(proba)
        start = time()
        result = genetic_algorithm(
            g,
            pool_size=200,
            selection_strategy="roulette",
            selection_percentage=0.6,
            crossing_proba=proba,
            crossing_manner="1",
            mutation_proba=0.5,
            nbr_iterations=40,
            param_tuning=True,
        )
        times.append(time() - start)
        if len(result) < num_iterations:
            result.extend([result[-1]] * (num_iterations - len(result)))
        min_optimum = min(min_optimum, min(result))
        max_optimum = max(max_optimum, max(result))
        axis[0].plot(iterations, result, label=str(proba))

        # re-init the the graph
        g.re_initialize_graph()

    print("times = ", times)
    print("iterations = ", iterations)
    print("optimums = ", result)
    
    axis[0].set_yticks(range(math.floor(0), math.ceil(max(times))))
    axis[0].set_yticks(range(math.floor(min_optimum), math.ceil(max_optimum)))
    axis[1].plot(probabilities, times)
    
    
    axis[0].legend()
    axis[1].legend()
    plt.savefig(
        f"./benchmark/genetic_algorithm/{file_name}/crossing_probability_impact.png", bbox_inches="tight"
    )
    plt.show()


def mutation_probability_impact(g):
    new_list = range(math.floor(0), math.ceil(g.num_vertices + 1))
    plt.yticks(new_list)

    num_iterations = 50
    probabilities = [0.0, 0.2, 0.5, 0.8, 1.0]
    iterations = list(range(num_iterations))

    for proba in probabilities:
        result = genetic_algorithm(
            g,
            pool_size=200,
            selection_strategy="roulette",
            selection_percentage=0.6,
            crossing_proba=0.6,
            crossing_manner="1",
            mutation_proba=proba,
            nbr_iterations=50,
            param_tuning=True,
        )

        if len(result) < num_iterations:
            result.extend([result[-1]] * (num_iterations - len(result)))
        plt.plot(iterations, result, label=str(proba))

        # re-init the the graph
        g.re_initialize_graph()

    plt.ylabel("optimal number of colors")
    plt.title("Impact of the mutation probability")
    plt.legend(loc="best")
    plt.savefig("./benchmark/mutation_probability_impact.png", bbox_inches="tight")
    plt.show()


def num_generations_impact(g):
    new_list = range(math.floor(0), math.ceil(g.num_vertices + 1))
    plt.yticks(new_list)

    num_generations = [_ for _ in range(20, 101, 20)]
    iterations = list(range(num_generations[-1]))

    for num in num_generations:
        result = genetic_algorithm(
            g,
            pool_size=200,
            selection_strategy="roulette",
            selection_percentage=0.6,
            crossing_proba=0.6,
            crossing_manner="1",
            mutation_proba=0.5,
            nbr_iterations=num,
            param_tuning=True,
        )

        if len(result) < num_generations[-1]:
            result.extend([result[-1]] * (num_generations[-1] - len(result)))
        plt.plot(iterations, result, label=str(num))

        # re-init the the graph
        g.re_initialize_graph()

    plt.ylabel("optimal number of colors")
    plt.title("Impact of the number of generations (iterations)")
    plt.legend(loc="best")
    plt.savefig("./benchmark/num_generations_impact.png", bbox_inches="tight")
    plt.show()


def pool_size_impact(g):
    new_list = range(math.floor(0), math.ceil(g.num_vertices + 1))
    plt.yticks(new_list)

    nbr_iterations = 45
    iterations = [_ for _ in range(nbr_iterations)]

    pool_sizes = [size for size in range(100, 701, 300)]
    for pool_size in pool_sizes:
        result = genetic_algorithm(
            g,
            pool_size=pool_size,
            selection_strategy="roulette",
            selection_percentage=0.6,
            crossing_proba=0.6,
            crossing_manner="1",
            mutation_proba=0.5,
            nbr_iterations=nbr_iterations,
            param_tuning=True,
        )

        if len(result) < nbr_iterations:
            result.extend([result[-1]] * (nbr_iterations - len(result)))
        plt.plot(iterations, result, label=str(pool_size))

        # re-init the the graph
        g.re_initialize_graph()

    plt.ylabel("optimal number of colors")
    plt.title("Impact of the pool size")
    plt.legend(loc="best")
    plt.savefig("./benchmark/pool_size_impact.png", bbox_inches="tight")
    plt.show()
