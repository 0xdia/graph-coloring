from cmath import inf
import time
from random import randint, shuffle, seed
from math import floor

seed(time.time())


def init_pack(wolf_size, pack_size):
    initial_pack = []
    initial_wolf = list(range(wolf_size))
    for _ in range(pack_size):
        shuffle(initial_wolf)
        initial_pack.append((wolf_size, initial_wolf.copy()))
    return initial_pack


def get_best_fitting(wolves):
    return wolves.index(min(wolves))


def improve_alpha(g, A, alpha_wolf):
    A = abs(A)
    for i in range(len(alpha_wolf[1])):
        rand_color = None
        if A > 1:
            rand_color = randint(g.num_vertices, floor(A * g.num_vertices))
        else:
            rand_color = randint(0, floor(A * g.num_vertices))
        candidate = alpha_wolf[1].copy()
        candidate[i] = rand_color
        if g.validate_candidate_solution(candidate):
            alpha_wolf[1][i] = rand_color
    return (len(set(alpha_wolf[1])), alpha_wolf[1])


def wolf_gain_experience(g, follower, *leaders):
    follower_colors = follower[1]
    leaders_colors = [leader[1] for leader in leaders]
    # treat alpha alone

    leaders_impact = [(2 + i, leaders_colors[i]) for i in range(len(leaders))] + [
        (1, follower_colors)
    ]

    # total impact
    sum_impacts = 1
    for i in range(len(leaders)):
        sum_impacts += 2 + i

    # shuffle impacts
    shuffle(leaders_impact)

    # proba maybe taken into account
    last_index = 0
    for slice in range(len(leaders_impact) - 1):
        begin_index = last_index
        last_index = (
            begin_index + (leaders_impact[slice][0] * g.num_vertices) // sum_impacts
        )
        candidate_sol = follower_colors.copy()
        candidate_sol[begin_index:last_index] = leaders_impact[slice][1][
            begin_index:last_index
        ]
        if g.validate_candidate_solution(candidate_sol):
            follower_colors[begin_index:last_index] = candidate_sol[
                begin_index:last_index
            ]

    begin_index = last_index
    candidate_sol = follower_colors.copy()
    candidate_sol[begin_index:] = leaders_impact[-1][1][begin_index:]
    if g.validate_candidate_solution(candidate_sol):
        follower_colors[begin_index:] = candidate_sol[begin_index:]

    return (len(set(follower_colors)), follower_colors)