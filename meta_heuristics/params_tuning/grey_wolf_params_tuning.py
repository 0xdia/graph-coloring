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
        "./benchmark/grey_wolf/" + file_name[:-4] + "/max_iter_impact_values.txt", "w+",
    ) as fp:
        fp.write("values, optimum, time\n")
        for (max_iter, optimum, t) in zip(max_iter_list, optimums, times):
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
    """plt.savefig(
        "./benchmark/grey_wolf/" + file_name[:-4] + "/max_iter_impact.png",
        bbox_inches="tight",
    )
    plt.show()
"""


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
    """with open("./benchmark/grey_wolf/" + file_name + "/pack_size.txt", "w+",) as fp:
        fp.write("values, optimum, time\n")
        for (max_iter, optimum, t) in zip(pack_size_list, optimums, times):
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
    """plt.savefig(
        "./benchmark/grey_wolf/" + file_name + "/pack_size_impact.png",
        bbox_inches="tight",
    )
    plt.show()"""


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
        "./benchmark/grey_wolf/" + {file_name} + "/a_param_impact_values.txt", "w+",
    ) as fp:
        fp.write("values, optimum, time\n")
        for (max_iter, optimum, t) in zip(a_param_list, optimums, times):
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
    """plt.savefig(
        "./benchmark/grey_wolf/" + {file_name} + "/a_param_impact.png",
        bbox_inches="tight",
    )
    plt.show()
"""
