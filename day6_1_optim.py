import resource
from itertools import product

global x1, y1, x2, y2, scores, candidates, iterations, grid


def get_distance(c1, c2):
    global iterations
    iterations += 1
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])


def get_best_candidate(candidates, c):
    best = 10000000000
    best_candidate = None
    has_dup = False
    for candidate, coords in candidates.items():
        d = get_distance(coords, c)
        if d < best:
            best = d
            best_candidate = candidate
            has_dup = False
        elif d == best:
            has_dup = True
    if has_dup:
        return '.'
    else:
        return best_candidate


def get_infinites(grid):
    global x1, y1, x2, y2
    result = set()
    for y in range(y1, y2+1):
        result.add(grid[x1, y])
        result.add(grid[x2, y])
    for x in range(x1, x2+1):
        result.add(grid[x, y1])
        result.add(grid[x, y2])
    return result


def build_grid_bourrin(candidates):
    global x1, y1, x2, y2, scores

    grid = {}

    for coord in product(range(x1, x2+1), range(y1, y2+1)):
        best_candidate = get_best_candidate(candidates, coord)
        grid[coord[0], coord[1]] = best_candidate
        if not best_candidate in scores:
            scores[best_candidate] = 1
        else:
            scores[best_candidate] += 1

    return grid


def get_tile(coords):
    if coords[0] < x1 or coords[0] > x2 or coords[1] < y1 or coords[1] > y2:
        return '.', False, coords

    c = grid.get(coords, None)
    marked = False
    if c is None:
        c = get_best_candidate(candidates, coords)
        grid[coords] = c
        marked = True
    return c, marked, coords


def get_view_matrix(coords, direction):
    if direction == 0:
        return [
            get_tile((coords[0] - 1, coords[1] - 1)),
            get_tile((coords[0], coords[1] - 1)),
            get_tile((coords[0] + 1, coords[1] - 1)),
        ]
    elif direction == 1:
        return [
            get_tile((coords[0], coords[1] - 1)),
            get_tile((coords[0] + 1, coords[1] - 1)),
            get_tile((coords[0] + 1, coords[1])),
        ]
    elif direction == 2:
        return [
            get_tile((coords[0] + 1, coords[1] - 1)),
            get_tile((coords[0] + 1, coords[1])),
            get_tile((coords[0] + 1, coords[1] + 1)),
        ]
    elif direction == 3:
        return [
            get_tile((coords[0] + 1, coords[1])),
            get_tile((coords[0] + 1, coords[1] + 1)),
            get_tile((coords[0], coords[1] + 1)),
        ]
    elif direction == 4:
        return [
            get_tile((coords[0] + 1, coords[1] + 1)),
            get_tile((coords[0], coords[1] + 1)),
            get_tile((coords[0] - 1, coords[1] + 1)),
        ]
    elif direction == 5:
        return [
            get_tile((coords[0], coords[1] + 1)),
            get_tile((coords[0] - 1, coords[1] + 1)),
            get_tile((coords[0] - 1, coords[1])),
        ]
    elif direction == 6:
        return [
            get_tile((coords[0] - 1, coords[1] + 1)),
            get_tile((coords[0] - 1, coords[1])),
            get_tile((coords[0] - 1, coords[1] - 1)),
        ]
    elif direction == 7:
        return [
            get_tile((coords[0] - 1, coords[1])),
            get_tile((coords[0] - 1, coords[1] - 1)),
            get_tile((coords[0], coords[1] - 1)),
        ]


def get_next_coords(coords, candidate, frontier, direction, initial_coords):
    fails = 0
    while fails < 8:
        matrix = get_view_matrix(coords, direction)
        if matrix[0][0] == candidate and matrix[0][2] not in frontier:
            direction = direction - 1 if direction > 0 else 7
            return matrix[0][2], direction
        is_different = matrix[0][0] != candidate
        if matrix[1][0] == candidate and matrix[1][2] not in frontier:
            return matrix[1][2], direction
        is_different = is_different or matrix[1][0] != candidate
        if matrix[2][0] == candidate and matrix[2][2] not in frontier:
            direction = direction + 1 if direction < 7 else 0
            return matrix[2][2], direction
        is_different = is_different or matrix[2][0] != candidate

        if not is_different:
            return None, None
        if initial_coords == matrix[0][2] or initial_coords == matrix[1][2] or initial_coords == matrix[2][2]:
            return None, None
        fails += 1
        direction = direction + 1 if direction < 7 else 0
    return None, None


def build_frontier(candidate, coords):
    global grid, candidates
    # algo :
    # 1. search frontier
    # 2. while we are not stuck,
    #   2.1. check right pos and if we can move right, next pos = right, break
    #   2.2. check up pos and if we can move up, next pos = up, break
    #   2.3. check left pos and if we can move left, next pos = left, break
    #   2.4. check down pos and if we can move down, next pos = down, break
    # Each time we can go to another tile, reset counter
    # Each time we can't go to another tile, inc counter
    # if counter == 4, we are stuck.

    # mark our position
    stuck = False
    frontier = []
    direction = 2
    while get_tile((coords[0] + 1, coords[1]))[0] == candidate:
        coords = (coords[0] + 1, coords[1])
    initial_coords = coords

    while not stuck:
        coords, direction = get_next_coords(coords, candidate, frontier, direction, initial_coords)
        stuck = coords is None
        if not stuck:
            frontier.append(coords)
        # if stuck and len(frontier) > 0:
        #     coords = frontier.pop()


def build_grid():
    global x1, y1, x2, y2, scores, grid

    for candidate, coords in candidates.items():
        build_frontier(candidate, coords)
        print("built %s" % candidate)
        # print_grid(grid)
    keys = sorted(grid.keys())

    s = {}
    last_k = None
    last_v = None
    for k in keys:
        v = grid.get(k, last_v)
        if last_k is not None:
            delta = 0
            if k[0] == last_k[0]:
                delta = k[1] - last_k[1]
            elif last_k[1] < y2:
                delta = y2 - last_k[1]
            if last_v not in s:
                s[last_v] = delta
            else:
                s[last_v] += delta

        last_k = k
        last_v = v

    for y in range(y1, y2+1):
        last_char = None
        for x in range(x1, x2+1):
            last_char = grid.get((x,y), last_char)
            if not last_char in scores:
                scores[last_char] = 1
            else:
                scores[last_char] += 1
    return grid


def get_largest_area(grid, scores):
    infinites = get_infinites(grid)
    best_candidate = None
    best_score = 0
    for candidate, score in scores.items():
        if candidate not in infinites and score > best_score:
            best_score = score
            best_candidate = candidate
    return best_candidate, best_score


def init_env(data):
    global x1, y1, x2, y2, scores, candidates, grid
    x1 = 1000000
    x2 = 0
    y1 = 1000000
    y2 = 0
    candidates = {}
    idx = 0
    for c in data:
        candidates[idx] = c
        if c[0] < x1:
            x1 = c[0]
        if c[0] > x2:
            x2 = c[0]
        if c[1] < y1:
            y1 = c[1]
        if c[1] > y2:
            y2 = c[1]
        idx += 1
    scores = {}
    grid = {}


def print_grid(grid):
    global x1, y1, x2, y2
    for y in range(y1, y2+1):
        line = ""
        for x in range(x1, x2+1):
            line = line + " %s" % grid.get((x, y), '?')
        print(line)
    print('-------')

data = (
    (10, 10),
    (10, 60),
    (80, 30),
    (30, 40),
    (50, 50),
    (80, 90),
)
#
# data = (
#     (152, 292),
#     (163, 90),
#     (258, 65),
#     (123, 147),
#     (342, 42),
#     (325, 185),
#     (69, 45),
#     (249, 336),
#     (92, 134),
#     (230, 241),
#     (74, 262),
#     (241, 78),
#     (299, 58),
#     (231, 146),
#     (239, 87),
#     (44, 157),
#     (156, 340),
#     (227, 226),
#     (212, 318),
#     (194, 135),
#     (235, 146),
#     (171, 197),
#     (160, 59),
#     (218, 205),
#     (323, 102),
#     (290, 356),
#     (244, 214),
#     (174, 250),
#     (70, 331),
#     (288, 80),
#     (268, 128),
#     (359, 98),
#     (78, 249),
#     (221, 48),
#     (321, 228),
#     (52, 225),
#     (151, 302),
#     (183, 150),
#     (142, 327),
#     (172, 56),
#     (72, 321),
#     (225, 298),
#     (265, 300),
#     (86, 288),
#     (78, 120),
#     (146, 345),
#     (268, 181),
#     (243, 235),
#     (262, 268),
#     (40, 60),
# )
#
# data = (
#     (1520, 2920),
#     (1630, 900),
#     (2580, 650),
#     (1230, 1470),
#     (3420, 420),
#     (690, 450),
#     (2490, 3360),
#     (920, 1340),
#     (2300, 2410),
#     (740, 2620),
#     (2410, 780),
#     (2990, 580),
#     (2310, 1460),
#     (2390, 870),
#     (440, 1570),
#     (1560, 3400),
#     (2270, 2260),
#     (2120, 3180),
#     (1940, 1350),
#     (2350, 1460),
#     (1710, 1970),
#     (1600, 590),
#     (2180, 2050),
#     (3230, 1020),
#     (2900, 3560),
#     (2440, 2140),
#     (1740, 2500),
#     (700, 3310),
#     (2880, 800),
#     (2680, 1280),
#     (3590, 980),
#     (780, 2490),
#     (2210, 480),
#     (3210, 2280),
#     (520, 2250),
#     (1510, 3020),
#     (1830, 1500),
#     (1420, 3270),
#     (1720, 560),
#     (720, 3210),
#     (2250, 2980),
#     (2650, 3000),
#     (860, 2880),
#     (780, 1200),
#     (1460, 3450),
#     (2680, 1810),
#     (2430, 2350),
#     (2620, 2680),
#     (400, 600),
# )

init_env(data)

iterations = 0
# grid = build_grid_bourrin(candidates)
#candidate, score = get_largest_area(grid, scores)

build_grid()
candidate, score = get_largest_area(grid, scores)

# print_grid(grid)

print("candidate : %s, score: %s, %s iterations" % (candidate, score, iterations))