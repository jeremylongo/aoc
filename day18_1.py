def get_new_val(m, x, y):
    current_val = m[y][x]
    neighbours = []
    maxx = len(m[y]) - 1
    maxy = len(m) - 1
    if y > 0:
        neighbours.append(m[y - 1][x])
        if x > 0:
            neighbours.append(m[y - 1][x - 1])
        if x < maxx:
            neighbours.append(m[y - 1][x + 1])
    if x > 0:
        neighbours.append(m[y][x - 1])
    if x < maxx:
        neighbours.append(m[y][x + 1])
    if y < maxy:
        neighbours.append(m[y + 1][x])
        if x > 0:
            neighbours.append(m[y + 1][x - 1])
        if x < maxx:
            neighbours.append(m[y + 1][x + 1])

    nbtrees = len([x for x in neighbours if x == '|'])
    nblumbyards = len([x for x in neighbours if x == '#'])
    # An open acre will become filled with trees if three or more adjacent acres contained trees.
    # Otherwise, nothing happens.
    if current_val == '.' and nbtrees >= 3:
        return '|'
    # An acre filled with trees will become a lumberyard if three or more adjacent acres were
    # lumberyards. Otherwise, nothing happens.
    if current_val == '|' and nblumbyards >= 3:
        return '#'
    # An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least
    # one other lumberyard and at least one acre containing trees.
    # Otherwise, it becomes open.
    if current_val == '#':
        if nblumbyards >= 1 and nbtrees >= 1:
            return '#'
        else:
            return '.'
    return current_val


def update_map(m):
    maxy = len(m) - 1
    maxx = len(m[0]) - 1
    res = []

    for y in range(0, maxy + 1):
        new_row = ''
        for x in range(0, maxx + 1):
            new_val = get_new_val(m, x, y)
            new_row += new_val
        res.append(new_row)

    return res


def print_map(m, r):
    print('round %s' % r)
    for row in m:
        print(row)
    print("")
    print("---------------------")


data = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

data = """..|#..#......#|.#..#|#.|##|.|.##.||..|.||....###|.
||.|....|#.#|.#...#.|...|#.#.#.#....#......#....#.
...#...|.....#.#..|#...||..#.|.|#....#|#|..##...|.
.....#....|#.|..|.....#|##...#.#.#||....||||....#.
..###...#.||.|||.##.#.|....|.##.#....|.#.|..|.....
....|..#.#.|...|..|.....#....#.#.......|.||...|...
#..|.....##|..#..#...#..|.##.....#......||##|.|#..
##........#...|#|.##.#|#..#|...#...#.##|||.#||..||
......#..|..|.#...|#||.#....#.#.|#.||......|.....|
.|...|.##....#.||...|..|..|.|........#.#..|||..|##
..|....|...#####..|#|..|...#...#.|...|..|.|..|.#|#
....|...#.#.#.......#......#.#|......#|.##..##.#|.
.....|.#..|#...||..#......|..#.|#.#|...#|.|..#||..
#....#.......|#.|..|...#...|..|.##|#.|#.#|.....|..
....#.||#.....#..#...|....##.#.......#.|.|||.|....
|.|..||##....|#..#..|..|.|.|..|||.##..#.|......##|
###..|.#|##|#.|||.#|.#..|#|..#..|.#|....#.#.#..||.
.|.....|#.#.|#||..#.....#.|.||.#.|.....|#..|...#..
...##.........|...#.#|....##..#.|.|.......#..|...|
..#.#.|.|.....||#..||...##||.#|..|.....#|...|...#|
....#...#||..|...|.|..|#.#.........|#...#.|||...#.
.#..|.##.|.|.#...#.....#.#.......|#.|.#||#.#.....#
|...#|..#....#...|.##.####....|#.##|#.#.|.....||..
....|.#.|#||..|#.|.|.#|...|.#....||.#...#|.#...|.#
.|..#.#..|#|..##..|.##..||...#...||....#||..#.|...
##......#.|...|.||.#.||....|.......#......##|#..|.
|#....#||....##...........#.|....|....|#|#.|..#...
..#...#|....|.|..|...#.......#.##.#.....#.||......
...|....#|#..#|...|...#|....#.#|.......|.......|#.
.#||..##||.|..|.|#..|.|....|.#|.|.|.....#.#.|..#.#
.....|..|...|...|......||...##.....##.......|.#..|
.....#..#|.#...#..#...||.|##..|#..##.|#.....##....
|...|.#||.........#..#..#||||....|...|..|..#...##.
#.#..|.|.......||..|#|..|....|.|#|#|.|..|.|...#.#.
#.|..||#.||||..###.|......|.#|||.##........||...||
.....#|..#.#.....|..|#.....|....|.#|||#.|.....#...
...||#..#...#...||#.||......|#..#..#.|#.|#|...|..#
.||.....||..|#.|#||...##..###|.#....|.|..|#...#|.|
...#.|#||..#.|||......#...||.#..|||..|#.|.##..#.|#
.#||..#.|||.......|.|#.....|.|#.#..##..|.|....|#..
..#.###..|.........|.....#..###|.|#..........#|.#|
#.||.|.#.|..||#|||#..##.|#....#.#.|.#.....|.|.#.|#
|..|..#.#..|.#.......#...#.|..|..|#..|..###|.||..|
|..|...||...|.#.#..##|.#..#...#|#..|.#..|.#..|.||.
..#.##..#.|..#.#..|..|#.|||.#..#..|#####.|..#.....
.|.|#.|#...||..##...#|#.........#...#|..##.#.#..#.
##|.|..#.#|....#..|..#....#......#||.|....||##..||
.##|#....#..#..#.....#|.#...#..#.|#||||.##.#....|.
..|.......#|....|#|..||..##..#.|#|..#.#|....|..#|#
....|||.|||#..||...|||.##..#.#|##....|..|..||..#|#"""

m = data.splitlines()

l = 0
t = 0
for minute in range(0, 10):
    m = update_map(m)
    print_map(m, minute)

l = 0
t = 0
for row in m:
    t += len([x for x in row if x == '|'])
    l += len([x for x in row if x == '#'])

print('trees : %s, lumberyards : %s, score: %s' % (t, l, t * l))
