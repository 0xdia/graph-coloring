from random import randint, seed
from time import time

seed(time()) # initialize the seed

def crossing(father, mother, manner="1point"):
    def uniform_crossing(father, mother):
        first_child, second_child = father.copy(), mother.copy()
        for i in range(len(father)):
            if randint(0, 1) == 1:
                first_child[i], second_child[i] = second_child[i], first_child[i]
        return first_child, second_child

    assert len(father) == len(mother)
    return (
        uniform_crossing(father, mother)
        if manner == "uniforme"
        else None  # k_points_croisement(father, mother, int(manner[0]))
    )
    pass


father = [1, 2, 3, 4, 5, 6]
mother = [10, 20, 30, 40, 50, 60]

first, second = crossing(father, mother, "uniforme")

print(father)
print(mother)
print(first)
print(second)