import numpy as np


def get_score(n):
    recipes = np.zeros(700000)
    recipes[0] = 3
    recipes[1] = 7

    idx1 = 0
    idx2 = 1
    last_idx = 1

    while last_idx < 10 + n:
        recipe_1 = recipes[idx1]
        recipe_2 = recipes[idx2]
        new_recipe = recipe_1 + recipe_2

        if new_recipe > 9:
            last_idx += 1
            recipes[last_idx] = int(new_recipe / 10)
        last_idx += 1
        recipes[last_idx] = new_recipe % 10

        idx1 = int(idx1 + recipe_1 + 1) % (last_idx + 1)
        idx2 = int(idx2 + recipe_2 + 1) % (last_idx + 1)

        # s = ""
        # for i in range(0, last_idx + 1):
        #     if i == idx1:
        #         s += "(%s) " % int(recipes[i])
        #     elif i == idx2:
        #         s += "[%s]" % int(recipes[i])
        #     else:
        #         s += " %s " % int(recipes[i])
        # print(s)

    score = "%s : " % n
    for i in range(n, n + 10):
        score = score + "%s" % int(recipes[i % (last_idx + 1)])
    print(score)


get_score(9)
get_score(5)
get_score(18)
get_score(2018)
get_score(681901)



