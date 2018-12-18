

class People(object):
    x = None
    y = None
    health = None
    # Ugly. Faster.
    race = ' '
    enemy_symbol = ' '
    neighbours = []
    distances = {}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.race = ' '
        self.health = 200
        self.neighbours = []
        self.distances = {}
        self.enemy_symbol = ' '

    def build_neighbours(self, world):
        self.neighbours = []
        checks = (
            (self.y, self.x - 1),
            (self.y - 1, self.x),
            (self.y, self.x + 1),
            (self.y + 1, self.x)
        )
        foe_char = self.enemy_symbol
        for check in checks:
            c = world.world[check[0]][check[1]]
            if c == '.' or c == foe_char:
                self.neighbours.append(check)

    def build_distances(self, world, foe):
        self.distances = {}
        if foe.race != self.race:
            best_neighbour = None
            best_d = None
            direction = None
            pkey = foe.key()
            if pkey in sorted(self.neighbours):
                best_neighbour = pkey
                best_d = 0
                direction = (0, 0)
            else:
                for neighbour in sorted(self.neighbours):
                    # build manhattan distance to other people
                    reachable = world.is_reachable(pkey, neighbour)
                    # if p is reachable
                    if reachable is not None:
                        d = abs(neighbour[0] - foe.y) + abs(neighbour[1] - foe.x)
                        if best_d is None or d < best_d:
                            best_neighbour = neighbour
                            best_d = d
                            direction = reachable
            if best_neighbour is not None:
                self.distances[pkey] = (best_neighbour, best_d, direction)

    def key(self):
        return self.y, self.x

    def move(self, direction, world):
        k = self.key()
        self.x += direction[1]
        self.y += direction[0]
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
        nearest = None
        foe_data = None
        distance = 0
        foe = None
        self_coords = self.key()
        keys = sorted(world.elves)
        for c in keys:
            foe = world.elves[c]
            data = foe.distances.get(self_coords, None)
            if data is not None and (nearest is None or data[1] < distance):
                nearest = foe
                foe_data = data
                distance = foe_data[1]
        return nearest, foe_data


class Elf(People):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.race = 'E'
        self.enemy_symbol = 'G'

    def get_nearest_foe(self, world):
        nearest = None
        foe_data = None
        distance = 0
        foe = None
        self_coords = self.key()
        keys = sorted(world.goblins)
        for c in keys:
            foe = world.goblins[c]
            data = foe.distances.get(self_coords, None)
            if data is not None and (nearest is None or data[1] < distance):
                nearest = foe
                foe_data = data
                distance = data[1]
        return nearest, foe_data


class World(object):
    world = []

    goblins = {}
    elves = {}
    peoples = {}

    def __init__(self, data):
        world = data.splitlines()
        for y in range(0, len(world)):
            row = world[y]
            for x in range(0, len(row)):
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
        is_reachable = True
        step = 1 if p2[1] > p1[1] else -1 if p2[1] < p1[1] else 0
        if step != 0:
            for x in range(p1[1], p2[1] + step, step):
                # ignore first loop
                if x != p1[1]:
                    is_reachable = is_reachable and self.world[p1[0]][x] == '.'
        stepy = 1 if p2[0] > p1[0] else -1 if p2[0] < p1[0] else 0
        if stepy != 0:
            for y in range(p1[0], p2[0] + stepy, stepy):
                if y != p1[0]:
                    is_reachable = is_reachable and self.world[y][p2[1]] == '.'
        if is_reachable:
            return (stepy, 0) if step == 0 else (0, step)

        is_reachable = True
        stepy = 1 if p2[0] > p1[0] else -1 if p2[0] < p1[0] else 0
        if stepy != 0:
            for y in range(p1[0], p2[0]+stepy, stepy):
                if y != p1[0]:
                    is_reachable = is_reachable and self.world[y][p2[1]] == '.'
        step = 1 if p2[1] > p1[1] else -1 if p2[1] < p1[1] else 0
        if step != 0:
            for x in range(p1[1], p2[1]+step, step):
                # ignore first loop
                if x != p1[1]:
                    is_reachable = is_reachable and self.world[p1[0]][x] == '.'
        if is_reachable:
            return (0, step) if stepy == 0 else (stepy, 0)
        return None

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
                for k, p in self.peoples.items():
                    if p.race != people.race:
                        p.build_neighbours(self)
                        p.build_distances(self, people)

                foe, foe_data = people.get_nearest_foe(self)
                if foe and foe_data:
                    print('%s at %s,%s (%s) nearest foe at %s,%s, distance=%s, moving %s,%s' % (c, x, y, people.health, foe.x, foe.y, foe_data[1], foe_data[2][1], foe_data[2][0]))
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

world = World(data)
world.draw()
r = 1
while world.can_turn():
    world.turn()
    print("round %s" % r)
    r += 1
    input()
