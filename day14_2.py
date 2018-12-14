import numpy as np


def get_score(n):
    data_size = 7000000
    recipes = np.zeros(data_size)
    recipes[0] = 3
    recipes[1] = 7

    idx1 = 0
    idx2 = 1
    last_idx = 1

    match_len = len(n)
    match = ""
    counter = 0
    while n not in match:
        counter += 1
        recipe_1 = recipes[idx1]
        recipe_2 = recipes[idx2]
        new_recipe = recipe_1 + recipe_2

        if new_recipe > 9:
            last_idx += 1
            i = int(new_recipe / 10)
            recipes[last_idx] = i
            match += chr(i + 48)
            match = match[-match_len:]
            if n == match:
                break

        last_idx += 1
        i = int(new_recipe % 10)
        recipes[last_idx] = i
        match += chr(i + 48)
        match = match[-match_len:]
        if n == match:
            break

        idx1 = int(idx1 + recipe_1 + 1) % (last_idx + 1)
        idx2 = int(idx2 + recipe_2 + 1) % (last_idx + 1)

        if data_size - last_idx < 10000:
            data_size += 1000000
            recipes.resize(data_size)
            print("resize : %s" % data_size)

    print("res=%s, idx1=%s, idx2=%s" % (last_idx-(match_len - 1), idx1, idx2))


get_score("51589")
get_score("01245")
get_score("92510")
get_score("59414")
get_score("681901")
