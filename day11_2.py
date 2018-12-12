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


row_cache = {}
zone_cache = {}
cells = {}


def get_row_score(x, y, size):
    # Check if we have a cache entry for this row
    cache_key = (x, y)
    if cache_key in row_cache[size]:
        return row_cache[size][cache_key]
    score = None

    # Check if we have a cache entry for the same row, smaller
    if score is None and (size - 1) in row_cache:
        key = (x, y)
        if key in row_cache[size - 1]:
            score = row_cache[size - 1][key]
            score += cells[(x + size - 1, y)]
    # Check if we have a cache entry for the same row, previous col
    if x > 1:
        key = (x - 1, y)
        if key in row_cache[size]:
            score = row_cache[size][key]
            score -= cells[(x - 1, y)]
            score += cells[(x + size - 1, y)]
    # Too bad, build entry
    if score is None:
        score = 0
        for i in range(x, x + size):
            score += cells[(i, y)]
    row_cache[size][cache_key] = score

    return score


def get_best_level(serial, minsize, maxsize):
    global cells
    global row_cache
    zone_cache = {}
    cells = {}
    row_cache = {}

    for cell_id in product(range(1, 301), range(1, 301)):
        cells[cell_id] = get_cell_value(serial, cell_id[0], cell_id[1])

    best_score = 0
    best = None
    best_size = 0
    for size in range(minsize, maxsize + 1):
        row_cache[size] = {}
        zone_cache[size] = {}
        for y in range(1, 302 - size):
            for x in range(1, 302 - size):
                score = None
                # Check if we have a zone cache entry for zone, one row up
                if y > 1:
                    key = (x, y - 1)
                    if key in zone_cache[size]:
                        score = zone_cache[size][key]
                        score -= get_row_score(x, y - 1, size)
                        score += get_row_score(x, y + size - 1, size)
                if score is None:
                    score = 0
                    for row_idx in range(y, y+size):
                        score += get_row_score(x, row_idx, size)
                zone_cache[size][(x,y)] = score
                if score > best_score:
                    best_score = score
                    best = (x, y)
                    best_size = size
        print("size=%s" % size)
    print("%s,%s,%s = %s" % (best[0], best[1], best_size, best_score))


print(get_cell_value(8, 3, 5))
print(get_cell_value(57, 122, 79))
print(get_cell_value(39, 217, 196))
print(get_cell_value(71, 101, 153))
get_best_level(18, 3, 3)
get_best_level(42, 3, 3)
get_best_level(7400, 3, 3)
get_best_level(7400, 3, 300)
