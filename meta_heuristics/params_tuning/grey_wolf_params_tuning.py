from inspect import Parameter
import math
import matplotlib.pyplot as plt
from time import time
import itertools
import numpy as np
from ..grey_wolf_optimizer.grey_wolf_optimizer import GWO


def max_iter_impact(g, file_name):
    figure, axis = plt.subplots(1, 2)
    axis[0].set_title("Nombres des couleurs optimums")
    axis[0].legend(loc="best")
    axis[0].set_xlabel("Iterations")
    axis[0].set_ylabel("Optimal number of colors")
    axis[1].set_title("Temps d'execution")
    axis[1].legend(loc="best")
    axis[1].set_xlabel("Maximum iterations")
    axis[1].set_ylabel("Temps d'execution")

    pack_size = 50
    a = 2
    max_iter_list = [_ for _ in range(250, 1001, 250)]
    iterations = list(range(max_iter_list[-1]))

    times = []
    optimums = []
    min_optimum, max_optimum = g.num_vertices, 0

    for max_iter in max_iter_list:
        print("max_iter = ", max_iter)
        start = time()
        result = GWO(g, max_iter, pack_size, a, True)
        times.append(time() - start)

        optimums.append(result[-1])

        result.extend([result[-1]] * (max_iter_list[-1] - max_iter))
        min_optimum = min(min_optimum, min(result))
        max_optimum = max(max_optimum, max(result))
        axis[0].plot(iterations, result, label=str(max_iter))

        # re-init the the graph
        g.re_initialize_graph()
    """with open(
        "./benchmark/grey_wolf/"+{file_name}+"/max_iter_impact_values.txt",
        "w+",
    ) as fp:
        fp.write("values, optimum, time\n")
        for (max_iter, optimum, t) in zip(
            max_iter_list, optimums, times
        ):
            fp.write("%s ,%s, %s\n" % (max_iter, optimum, t))
        fp.close()
"""
    axis[0].set_yticks(range(math.floor(0), math.ceil(max(times))))
    axis[0].set_yticks(range(math.floor(min_optimum), math.ceil(max_optimum)))
    axis[0].set_ylim(bottom=min_optimum - 1, top=max_optimum)
    axis[1].plot(max_iter_list, times)

    axis[0].legend()
    axis[1].legend()
    plt.show()
    plt.savefig(
        "./benchmark/tabu_search/" + {file_name} + "/max_iter_impact.png",
        bbox_inches="tight",
    )
    plt.show()


def pack_size_impact(g, file_name):
    figure, axis = plt.subplots(1, 2)
    axis[0].set_title("Nombres des couleurs optimums")
    axis[0].legend(loc="best")
    axis[0].set_xlabel("Iterations")
    axis[0].set_ylabel("Optimal number of colors")
    axis[1].set_title("Temps d'execution")
    axis[1].legend(loc="best")
    axis[1].set_xlabel("Pack size")
    axis[1].set_ylabel("Temps d'execution")

    pack_size_list = [_ for _ in range(25, 200, 25)]
    a = 2
    max_iter = 500
    iterations = list(range(max_iter))

    times = []
    optimums = []
    min_optimum, max_optimum = g.num_vertices, 0

    for pack_size in pack_size_list:
        print("pack_size = ", pack_size)
        start = time()
        result = GWO(g, max_iter, pack_size, a, True)
        times.append(time() - start)

        optimums.append(result[-1])

        min_optimum = min(min_optimum, min(result))
        max_optimum = max(max_optimum, max(result))
        axis[0].plot(iterations, result, label=str(pack_size))

        # re-init the the graph
        g.re_initialize_graph()
    """with open(
        "./benchmark/grey_wolf/"+{file_name}+"/max_iter_impact_values.txt",
        "w+",
    ) as fp:
        fp.write("values, optimum, time\n")
        for (max_iter, optimum, t) in zip(
            max_iter_list, optimums, times
        ):
            fp.write("%s ,%s, %s\n" % (max_iter, optimum, t))
        fp.close()
"""
    axis[0].set_yticks(range(math.floor(0), math.ceil(max(times))))
    axis[0].set_yticks(range(math.floor(min_optimum), math.ceil(max_optimum)))
    axis[0].set_ylim(bottom=min_optimum - 1, top=max_optimum)
    axis[1].plot(pack_size_list, times)

    axis[0].legend()
    axis[1].legend()
    plt.show()
    plt.savefig(
        "./benchmark/tabu_search/" + {file_name} + "/max_iter_impact.png",
        bbox_inches="tight",
    )
    plt.show()


def a_param_impact(g, file_name):
    figure, axis = plt.subplots(1, 2)
    axis[0].set_title("Nombres des couleurs optimums")
    axis[0].legend(loc="best")
    axis[0].set_xlabel("Iterations")
    axis[0].set_ylabel("Optimal number of colors")
    axis[1].set_title("Temps d'execution")
    axis[1].legend(loc="best")
    axis[1].set_xlabel("Pack size")
    axis[1].set_ylabel("Temps d'execution")

    a_param_list = [1, 2, 3, 4, 5]
    pack_size = 150
    max_iter = 500
    iterations = list(range(max_iter))

    times = []
    optimums = []
    min_optimum, max_optimum = g.num_vertices, 0

    for a_param in a_param_list:
        print("a paramater = ", a_param)
        start = time()
        result = GWO(g, max_iter, pack_size, a_param, True)
        times.append(time() - start)

        optimums.append(result[-1])

        min_optimum = min(min_optimum, min(result))
        max_optimum = max(max_optimum, max(result))
        axis[0].plot(iterations, result, label=str(a_param))

        # re-init the the graph
        g.re_initialize_graph()
    """with open(
        "./benchmark/grey_wolf/"+{file_name}+"/max_iter_impact_values.txt",
        "w+",
    ) as fp:
        fp.write("values, optimum, time\n")
        for (max_iter, optimum, t) in zip(
            max_iter_list, optimums, times
        ):
            fp.write("%s ,%s, %s\n" % (max_iter, optimum, t))
        fp.close()
"""
    axis[0].set_yticks(range(math.floor(0), math.ceil(max(times))))
    axis[0].set_yticks(range(math.floor(min_optimum), math.ceil(max_optimum)))
    axis[0].set_ylim(bottom=min_optimum - 1, top=max_optimum)
    axis[1].plot(a_param_list, times)

    axis[0].legend()
    axis[1].legend()
    plt.show()
    plt.savefig(
        "./benchmark/tabu_search/" + {file_name} + "/max_iter_impact.png",
        bbox_inches="tight",
    )
    plt.show()


"""
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

    with open("./benchmark/tabu_search/games120/reps_impact_values.txt", "w+") as fp:
        fp.write("values, optimum, time\n")
        for (reps_impact, optimum, t) in zip(reps_list, optimums, times):
            fp.write("%s ,%s, %s\n" % (reps_impact, optimum, t))

    axis[0].plot(reps_list, optimums)
    axis[1].plot(reps_list, times)
    axis[0].legend()
    axis[1].legend()
    plt.legend(loc="best")
    plt.savefig("./benchmark/tabu_search/games120/reps_impact.png", bbox_inches="tight")
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
        "./benchmark/tabu_search/games120/max_iterations_impact_values.txt", "w+"
    ) as fp:
        fp.write("values, optimum, time\n")
        for (max_iterations, optimum, t) in zip(max_iterations_list, optimums, times):
            fp.write("%s ,%s, %s\n" % (max_iterations, optimum, t))

    axis[0].plot(max_iterations_list, optimums)
    axis[1].plot(max_iterations_list, times)
    axis[0].legend()
    axis[1].legend()
    plt.legend(loc="best")
    plt.savefig(
        "./benchmark/tabu_search/games120/max_iterations_impact.png",
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
        "./benchmark/tabu_search/games120/tabu_size_impact_values.txt", "w+"
    ) as fp:
        fp.write("values, optimum, time\n")
        for (tabu_size, optimum, t) in zip(tabu_size_list, optimums, times):
            fp.write("%s ,%s, %s\n" % (tabu_size, optimum, t))

    axis[0].plot(tabu_size_list, optimums)
    axis[1].plot(tabu_size_list, times)
    axis[0].legend()
    axis[1].legend()
    plt.legend(loc="best")
    plt.savefig(
        "./benchmark/tabu_search/games120/tabu_size_impact.png", bbox_inches="tight"
    )
    plt.show()
"""
