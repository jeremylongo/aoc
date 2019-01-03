target_y = 10
target_x = 10
depth = 510


target_x = 15
target_y = 700
depth = 4848

cave = {}


def get_erosion(cave, depth, x, y, tx, ty):
    idx = 0
    if (x == 0 and y == 0) or (x == tx and y == ty):
        idx = 0
    elif y == 0:
        idx = x * 16807
    elif x == 0:
        idx = y * 48271
    else:
        idx = cave[(x-1, y)] * cave[(x, y-1)]
    erosion = (idx + depth) % 20183
    cave[(x, y)] = erosion
    return erosion

risk = 0

for y in range (0, target_y + 1):
    for x in range(0, target_x + 1):
        erosion = get_erosion(cave, depth, x, y, target_x, target_y)
        risk += erosion % 3

print("risk: %s" % risk)