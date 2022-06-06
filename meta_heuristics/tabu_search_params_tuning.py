import math
import matplotlib.pyplot as plt
from time import time
import itertools
import numpy as np
from .tabu_search import tabucol


def number_of_colors_impact(g):
    figure, axis = plt.subplots(1, 2)
    axis[0].set_title("Nombres des couleurs optimums")
    axis[0].legend(loc="best")
    axis[0].set_yticks(range(math.floor(0), math.ceil(g.num_vertices + 1), 5))
    axis[1].set_title("Temps d'execution")
    axis[1].legend(loc="best")

    reps = 400
    max_iterations = 10000
    number_of_colors_list = list(range(40, 500, 5))
    tabu_size = 7
    optimums = []
    times = []
    for number_of_colors in number_of_colors_list:
        start = time()
        tabucol(g, number_of_colors, tabu_size, reps, max_iterations, debug=False)
        optimums.append(g.optimum)
        times.append(time() - start)

        # re-init the the graph
        g.re_initialize_graph()

    with open(
        "./benchmark/tabu_search/mulsol.i.4/initial_number_of_colors_impact_values.txt",
        "w+",
    ) as fp:
        for (optimum, t) in zip(optimums, times):
            fp.write("%s, %s\n" % (optimum, t))

    axis[0].plot(number_of_colors_list, optimums)
    axis[1].plot(number_of_colors_list, times)
    axis[0].legend()
    axis[1].legend()
    plt.legend(loc="best")
    plt.savefig(
        "./benchmark/tabu_search/mulsol.i.4/initial_number_of_colors_impact.png",
        bbox_inches="tight",
    )
    plt.show()


def reps_impact(g):
    figure, axis = plt.subplots(1, 2)
    axis[0].set_title("Nombres des couleurs optimums")
    axis[0].legend(loc="best")
    axis[0].set_yticks(range(math.floor(0), math.ceil(g.num_vertices + 1)))
    axis[1].set_title("Temps d'execution")
    axis[1].legend(loc="best")

    reps_list = list(range(25, 500, 25))
    max_iterations = 10000
    number_of_colors = 200
    tabu_size = 7
    optimums = []
    times = []
    for reps in reps_list:
        start = time()
        tabucol(g, number_of_colors, tabu_size, reps, max_iterations, debug=False)
        optimums.append(g.optimum)
        times.append(time() - start)

        # re-init the the graph
        g.re_initialize_graph()

    with open("./benchmark/tabu_search/mulsol.i.4/reps_impact_values.txt", "w+") as fp:
        for (optimum, t) in zip(optimums, times):
            fp.write("%s, %s\n" % (optimum, t))

    axis[0].plot(reps_list, optimums)
    axis[1].plot(reps_list, times)
    axis[0].legend()
    axis[1].legend()
    plt.legend(loc="best")
    plt.savefig(
        "./benchmark/tabu_search/mulsol.i.4/reps_impact.png", bbox_inches="tight"
    )
    plt.show()


def max_iterations_impact(g):
    figure, axis = plt.subplots(1, 2)
    axis[0].set_title("Nombres des couleurs optimums")
    axis[0].legend(loc="best")
    axis[0].set_yticks(range(math.floor(0), math.ceil(g.num_vertices + 1)))
    axis[1].set_title("Temps d'execution")
    axis[1].legend(loc="best")

    reps = 400
    max_iterations_list = list(range(5000, 50000, 1000))
    number_of_colors = 200
    tabu_size = 7
    optimums = []
    times = []
    for max_iterations in max_iterations_list:
        start = time()
        tabucol(g, number_of_colors, tabu_size, reps, max_iterations, debug=False)
        optimums.append(g.optimum)
        times.append(time() - start)

        # re-init the the graph
        g.re_initialize_graph()
    with open(
        "./benchmark/tabu_search/mulsol.i.4/max_iterations_impact_values.txt", "w+"
    ) as fp:
        for (optimum, t) in zip(optimums, times):
            fp.write("%s, %s\n" % (optimum, t))

    axis[0].plot(max_iterations_list, optimums)
    axis[1].plot(max_iterations_list, times)
    axis[0].legend()
    axis[1].legend()
    plt.legend(loc="best")
    plt.savefig(
        "./benchmark/tabu_search/mulsol.i.4/max_iterations_impact.png",
        bbox_inches="tight",
    )
    plt.show()


def tabu_size_impact(g):
    figure, axis = plt.subplots(1, 2)
    axis[0].set_title("Nombres des couleurs optimums")
    axis[0].legend(loc="best")
    axis[0].set_yticks(range(math.floor(0), math.ceil(g.num_vertices + 1)))
    axis[1].set_title("Temps d'execution")
    axis[1].legend(loc="best")

    reps = 400
    max_iterations = 10000
    number_of_colors = 200
    tabu_size_list = list(range(1, 30, 1))
    optimums = []
    times = []
    for tabu_size in tabu_size_list:
        start = time()
        tabucol(g, number_of_colors, tabu_size, reps, max_iterations, debug=False)
        optimums.append(g.optimum)
        times.append(time() - start)

        # re-init the the graph
        g.re_initialize_graph()
    with open(
        "./benchmark/tabu_search/mulsol.i.4/tabu_size_impact_values.txt", "w+"
    ) as fp:
        for (optimum, t) in zip(optimums, times):
            fp.write("%s, %s\n" % (optimum, t))

    axis[0].plot(tabu_size_list, optimums)
    axis[1].plot(tabu_size_list, times)
    axis[0].legend()
    axis[1].legend()
    plt.legend(loc="best")
    plt.savefig(
        "./benchmark/tabu_search/mulsol.i.4/tabu_size_impact.png", bbox_inches="tight"
    )
    plt.show()
