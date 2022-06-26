from .operators import init_pack, get_best_fitting, wolf_gain_experience, improve_alpha
import time
from random import seed, random

seed(time.time())


def GWO(g, max_iter, pack_size):
    g.optimum = g.num_vertices
    print("g.vertices ", g.num_vertices)
    wolves = init_pack(g.num_vertices, pack_size)
    alpha, beta, delta = 0, 1, 2
    a, A = 2, 0
    start_time = time.time()
    for iter in range(max_iter):
        # print(f"[+] Iter {iter}")
        A = 2 * a * random() - a
        # print("A = ", A)
        wolves[alpha] = improve_alpha(g, A, wolves[alpha])
        wolves[beta] = wolf_gain_experience(g, wolves[beta], wolves[alpha])
        wolves[delta] = wolf_gain_experience(
            g, wolves[delta], wolves[beta], wolves[alpha]
        )

        # print(f"{alpha}, {beta}, {delta}")

        for wolf in range(pack_size):
            if wolf in [alpha, beta, delta]:
                continue
            wolves[wolf] = wolf_gain_experience(
                g, wolves[wolf], wolves[delta], wolves[beta], wolves[alpha]
            )

        best_fitting = get_best_fitting(wolves)

        if wolves[best_fitting][0] < wolves[alpha][0]:
            if best_fitting == beta:
                alpha, beta = best_fitting, alpha
            elif best_fitting == delta:
                alpha, delta == best_fitting, alpha
            else:
                alpha = best_fitting
            g.update_solution(wolves[alpha][1])
            # print("alpha updated")
        elif wolves[best_fitting][0] < wolves[beta][0]:
            beta = best_fitting
            # print("beta updated")
        elif wolves[best_fitting][0] < wolves[delta][0]:
            delta = best_fitting
            # print("delta updated")

        a = 2 * (1 - iter / max_iter)

    end_time =time.time()
    g.validate_solution()
    print("wolves alpha ", wolves[alpha][0])
    print("g.optimum ", g.optimum)
    return g.optimum , end_time-start_time