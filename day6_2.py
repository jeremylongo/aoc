from itertools import product

global x1, y1, x2, y2, scores, candidates, iterations


def get_distance(c1, c2):
    global iterations
    iterations += 1
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])


def init_env(data):
    global x1, y1, x2, y2, scores, candidates
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


def get_ranged_region_size(candidates, max_range):
    global x1, y1, x2, y2, scores
    total_size = 0

    for coord in product(range(x1, x2+1), range(y1, y2+1)):
        total_distance = sum([get_distance(coord, candidate_coord) for candidate, candidate_coord in candidates.items()])

        if total_distance < max_range:
            total_size += 1
    return total_size


def print_grid(grid):
    global x1, y1, x2, y2
    for y in range(y1, y2+1):
        line = ""
        for x in range(x1, x2+1):
            line = line + " %s" % grid[x, y]
        print(line)


# data = (
#     (1, 1),
#     (1, 6),
#     (8, 3),
#     (3, 4),
#     (5, 5),
#     (8, 9),
# )

data = (
    (152, 292),
    (163, 90),
    (258, 65),
    (123, 147),
    (342, 42),
    (325, 185),
    (69, 45),
    (249, 336),
    (92, 134),
    (230, 241),
    (74, 262),
    (241, 78),
    (299, 58),
    (231, 146),
    (239, 87),
    (44, 157),
    (156, 340),
    (227, 226),
    (212, 318),
    (194, 135),
    (235, 146),
    (171, 197),
    (160, 59),
    (218, 205),
    (323, 102),
    (290, 356),
    (244, 214),
    (174, 250),
    (70, 331),
    (288, 80),
    (268, 128),
    (359, 98),
    (78, 249),
    (221, 48),
    (321, 228),
    (52, 225),
    (151, 302),
    (183, 150),
    (142, 327),
    (172, 56),
    (72, 321),
    (225, 298),
    (265, 300),
    (86, 288),
    (78, 120),
    (146, 345),
    (268, 181),
    (243, 235),
    (262, 268),
    (40, 60),
)

init_env(data)
iterations = 0
print(get_ranged_region_size(candidates, 10000))
