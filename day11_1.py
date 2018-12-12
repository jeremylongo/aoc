from itertools import product


def get_cell_value(serial, x, y):
    # rackid = x + 10
    # power = third digit of (((rackid + 10) * y) + serial ) * rackid
    # rack_id = x + 10
    # p = rack_id * y
    # p += serial
    # p *= rack_id
    # digit = int(p / 100) % 10
    # p = digit - 5
    res = (int(((((x + 10) * y) + serial) * (x + 10)) / 100) % 10) - 5
    return res

def get_best_level(serial):
    cells = {}
    for cell_id in product(range(1, 301), range(1, 301)):
        cells[cell_id] = get_cell_value(serial, cell_id[0], cell_id[1])

    best_score = 0
    best = None
    for y in range(1, 299):
        for x in range(1, 299):
            score = cells[(x,y)] + cells[(x+1,y)] + cells[(x+2,y)] \
                    + cells[(x,y+1)] + cells[(x+1,y+1)] + cells[(x+2,y+1)] \
                    + cells[(x,y+2)] + cells[(x+1,y+2)] + cells[(x+2,y+2)]
            if score > best_score:
                best_score = score
                best = (x, y)

    print("%s,%s = %s" % (best[0], best[1], best_score))


print(get_cell_value(8, 3, 5))
print(get_cell_value(57, 122, 79))
print(get_cell_value(39, 217, 196))
print(get_cell_value(71, 101, 153))
get_best_level(18)
get_best_level(42)
get_best_level(7400)
