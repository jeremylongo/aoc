import copy
from collections import deque


class People(object):
    x = None
    y = None
    health = None
    # Ugly. Faster.
    race = ' '
    enemy_symbol = ' '
    neighbours = []
    distances = {}
    dist_map = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.race = ' '
        self.health = 200
        self.neighbours = []
        self.distances = {}
        self.dist_map = []
        self.enemy_symbol = ' '

    def build_neighbours(self, world):
        # build list of available neighbours
        self.neighbours = []
        checks = (
            (self.y, self.x - 1),
            (self.y - 1, self.x),
            (self.y + 1, self.x),
            (self.y, self.x + 1),
        )
        foe_char = self.enemy_symbol
        for check in checks:
            if check[0] < world.maxy and check[1] < world.maxx:
                c = world.world[check[0]][check[1]]
                if c == '.' or c == foe_char:
                    self.neighbours.append(check)

    def build_distance_map(self, world, from_coord):
        w = []
        q = deque([from_coord])
        for row in world.world:
            w.append(list(row))

        r = {from_coord: from_coord, }

        maxy = world.maxy
        maxx = world.maxx
        if w[from_coord[0]][from_coord[1]] == '.':
            w[from_coord[0]][from_coord[1]] = 1
            while len(q) > 0:
                item = q.popleft()
                y = item[0]
                x = item[1]
                step = w[y][x] + 1

                c = (y-1, x)
                if y > 0 and w[y-1][x] == '.' and not c in r:
                    q.append(c)
                    r[c] = c
                    w[y-1][x] = step
                c = (y+1, x)
                if y < maxy and w[y+1][x] == '.' and not c in r:
                    q.append(c)
                    r[c] = c
                    w[y+1][x] = step
                c = (y, x-1)
                if x > 0 and w[y][x-1] == '.' and not c in r:
                    q.append(c)
                    r[c] = c
                    w[y][x-1] = step
                c = (y, x+1)
                if x < maxx and w[y][x+1] == '.' and not c in r:
                    q.append(c)
                    r[c] = c
                    w[y][x+1] = step
        # for row in w:
        #     print(''.join([chr(ord('0')+c) if isinstance(c, int) else c for c in row]))
        return w

    def is_reachable(self, world, from_coord):
        checks = (
            (self.y, self.x - 1),
            (self.y - 1, self.x),
            (self.y + 1, self.x),
            (self.y, self.x + 1),
        )

        best = None
        best_d = 0
        w = self.build_distance_map(world, from_coord)
        for check in checks:
            if check[0] < world.maxy and check[1] < world.maxx:
                c = w[check[0]][check[1]]
                if isinstance(c, int) and (best is None or c < best_d):
                    best = check
                    best_d = c
        if best is None:
            return None, None
        else:
            return best, best_d

    def build_distances(self, world, foe):
        # build distances data from enemy to our neighbours
        self.distances = {}
        pos = None
        if foe.race != self.race:
            best_neighbour = None
            best_d = None
            direction = None
            pkey = foe.key()
            # build propagation distances from foe to any point
            if pkey in self.neighbours:
                best_neighbour = pkey
                best_d = 0
                pos = self.key()
            else:
                for neighbour in self.neighbours:
                    # check if foe can get to the neighbour
                    reachable, d = foe.is_reachable(world, neighbour)
                    # if p is reachable
                    if reachable is not None:
                        if best_d is None or d < best_d:
                            best_neighbour = neighbour
                            best_d = d
                            pos = reachable
            if best_neighbour is not None:
                self.distances[pkey] = (best_neighbour, best_d, pos)

    def key(self):
        return self.y, self.x

    def move(self, newpos, world):
        k = self.key()
        self.x = newpos[1]
        self.y = newpos[0]
        new_k = self.key()
        if k in world.elves:
            del (world.elves[k])
            world.elves[new_k] = self
        if k in world.goblins:
            del (world.goblins[k])
            world.goblins[new_k] = self
        if k in world.peoples:
            del (world.peoples[k])
            world.peoples[new_k] = self
        c = world.world[k[0]][k[1]]
        s = world.world[k[0]]
        s = s[:k[1]] + '.' + s[k[1] + 1:]
        world.world[k[0]] = s
        s = world.world[new_k[0]]
        s = s[:new_k[1]] + c + s[new_k[1] + 1:]
        world.world[new_k[0]] = s

    def attack(self, foe, world):
        foe.health -= 3
        if foe.health <= 0:
            k = foe.key()
            if k in world.elves:
                del (world.elves[k])
            if k in world.goblins:
                del (world.goblins[k])
            if k in world.peoples:
                del (world.peoples[k])
            s = world.world[k[0]]
            s = s[:k[1]] + '.' + s[k[1] + 1:]
            world.world[k[0]] = s
        return


class Goblin(People):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_symbol = 'E'
        self.race = 'G'

    def get_nearest_foe(self, world):
        nearest = []
        foe_data = None
        distance = 0
        foe = None
        self_coords = self.key()
        keys = sorted(world.elves)
        for c in keys:
            foe = world.elves[c]
            data = foe.distances.get(self_coords, None)
            if data is not None and (len(nearest) == 0 or data[1] <= distance):
                if data[1] < distance:
                    nearest = []
                nearest.append((foe, data))
                distance = data[1]
        weakest = None
        health = 1000
        for foe, data in nearest:
            if foe.health < health:
                weakest = foe
                foe_data = data
                health = foe.health
        return weakest, foe_data


class Elf(People):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.race = 'E'
        self.enemy_symbol = 'G'

    def get_nearest_foe(self, world):
        nearest = []
        foe_data = None
        distance = 0
        foe = None
        self_coords = self.key()
        keys = sorted(world.goblins)
        for c in keys:
            foe = world.goblins[c]
            data = foe.distances.get(self_coords, None)
            if data is not None and (len(nearest) == 0 or data[1] <= distance):
                if data[1] < distance:
                    nearest = []
                nearest.append((foe, data))
                distance = data[1]
        weakest = None
        health = 1000
        for foe, data in nearest:
            if foe.health < health:
                weakest = foe
                foe_data = data
                health = foe.health
        return weakest, foe_data


class World(object):
    world = []

    goblins = {}
    elves = {}
    peoples = {}
    maxx = 0
    maxy = 0

    def __init__(self, data):
        world = data.splitlines()
        self.maxy = len(world)
        for y in range(0, self.maxy):
            row = world[y]
            self.maxx = len(row)
            for x in range(0, self.maxx):
                c = row[x]
                key = (y, x)
                if c == 'G':
                    goblin = Goblin(x, y)
                    self.goblins[key] = goblin
                    self.peoples[key] = goblin
                elif c == 'E':
                    elf = Elf(x, y)
                    self.elves[key] = elf
                    self.peoples[key] = elf
        self.world = world

    def is_reachable(self, p1, p2):
        # is_reachable = True
        # step = 1 if p2[1] > p1[1] else -1 if p2[1] < p1[1] else 0
        # if step != 0:
        #     for x in range(p1[1], p2[1] + step, step):
        #         # ignore first loop
        #         if x != p1[1]:
        #             is_reachable = is_reachable and self.world[p1[0]][x] == '.'
        # stepy = 1 if p2[0] > p1[0] else -1 if p2[0] < p1[0] else 0
        # if stepy != 0:
        #     for y in range(p1[0], p2[0] + stepy, stepy):
        #         if y != p1[0]:
        #             is_reachable = is_reachable and self.world[y][p2[1]] == '.'
        # if is_reachable:
        #     return (stepy, 0) if step == 0 else (0, step)
        #
        # is_reachable = True
        # stepy = 1 if p2[0] > p1[0] else -1 if p2[0] < p1[0] else 0
        # if stepy != 0:
        #     for y in range(p1[0], p2[0]+stepy, stepy):
        #         if y != p1[0]:
        #             is_reachable = is_reachable and self.world[y][p2[1]] == '.'
        # step = 1 if p2[1] > p1[1] else -1 if p2[1] < p1[1] else 0
        # if step != 0:
        #     for x in range(p1[1], p2[1]+step, step):
        #         # ignore first loop
        #         if x != p1[1]:
        #             is_reachable = is_reachable and self.world[p1[0]][x] == '.'
        # if is_reachable:
        #     return (0, step) if stepy == 0 else (stepy, 0)
        # return None
        steps = copy.deepcopy(self.world)

    def can_turn(self):
        return len(self.goblins) > 0 and len(self.elves) > 0

    def draw(self):
        for y in range(0, len(self.world)):
            print(self.world[y])
        print("----------------------")

    def turn(self):
        keys = sorted(self.peoples)
        for key in keys:
            people = self.peoples.get(key, None)
            if people:
                y = key[0]
                x = key[1]
                row = self.world[y]
                c = row[x]
                for k, foe in self.peoples.items():
                    if foe.race != people.race:
                        foe.build_neighbours(self)
                        foe.build_distances(self, people)

                foe, foe_data = people.get_nearest_foe(self)
                if foe and foe_data:
#                    print('%s at %s,%s (%s) nearest foe at %s,%s, distance=%s, moving %s,%s' % (c, x, y, people.health, foe.x, foe.y, foe_data[1], foe_data[2][1], foe_data[2][0]))
                    if foe_data[1] > 0 and foe_data[2]:
                        people.move(foe_data[2], self)
                    if foe_data[1] <= 1:
                        people.attack(foe, self)
        self.draw()


data = """#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########
"""

data = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""

data = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""

data = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""

data = """#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
"""

data = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
"""

data = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
"""

data = """################################
######......###...##..##########
######....#G###G..##.G##########
#####...G##.##.........#########
##....##..#.##...........#######
#....#G.......##.........G.#####
##..##GG....G.................##
##.......G............#.......##
###.....G.....G#......E.......##
##......##....................##
#.....####......G.....#...######
#.#########.G....G....#E.#######
###########...#####......#######
###########..#######..E.......##
###########.#########......#.###
########..#.#########.........##
#######G....#########........###
##.##.#.....#########...EE#..#.#
#...GG......#########.#...##..E#
##...#.......#######..#...#....#
###.##........#####......##...##
###.........................#..#
####.............##........###.#
####............##.........#####
####..##....###.#...#.....######
########....###..............###
########..G...##.###...E...E.###
#########...G.##.###.E....E.####
#########...#.#######.......####
#############..########...######
##############.########.########
################################"""

data = """################################
#########################.G.####
#########################....###
##################.G.........###
##################.##.......####
#################...#.........##
################..............##
######..########...G...#.#....##
#####....######.G.GG..G..##.####
#######.#####G............#.####
#####.........G..G......#...####
#####..G......G..........G....##
######GG......#####........E.###
#######......#######..........##
######...G.G#########........###
######......#########.....E..###
#####.......#########........###
#####....G..#########........###
######.##.#.#########......#####
#######......#######.......#####
#######.......#####....E...#####
##.G..#.##............##.....###
#.....#........###..#.#.....####
#.........E.E...#####.#.#....###
######......#.....###...#.#.E###
#####........##...###..####..###
####...G#.##....E####E.####...##
####.#########....###E.####....#
###...#######.....###E.####....#
####..#######.##.##########...##
####..######################.###
################################
"""

world = World(data)
world.draw()
r = 1
outcome = 0
while world.can_turn():
    print("after %s round" % r)
    world.turn()
    print('health after : ' + ', '.join(["%s" % world.peoples[p].health for p in sorted(world.peoples.keys())]))
    # for k in :
    #     print(world.peoples[k].health)
    outcome = (r - 1) * sum([p.health for k, p in world.peoples.items()])
    r += 1

print(outcome)
print(', '.join(["%s" % world.peoples[p].health for p in sorted(world.peoples.keys())]))
