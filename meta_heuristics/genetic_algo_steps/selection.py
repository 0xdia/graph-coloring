import time
from random import seed, uniform

from .helper_functions import elitist, random, ranking, roulette, tournament

seed(time.time())


def selection(population, strategy="random", percentage=0.5):
    assert 0.0 < percentage and percentage < 1.0
    # this could be replaced with match-case introduced in python 3.10
    return {
        "roulette": roulette(population, percentage),
        "elitist": elitist(population),
        "tournament": tournament(population),
        "ranking": ranking(population),
        "random": random(population),
    }[strategy]
