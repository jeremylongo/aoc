def evolve(s, patterns):
    s = '..' + s + '....'
    res = ""
    for i in range(2, len(s) - 2):
        sample = s[i-2:i+3]
        if sample in patterns:
            res += patterns[sample]
        else:
            res += '.'
    return res.rstrip('.')

# patterns = {
#     '...##': '#',
#     '..#..': '#',
#     '.#...': '#',
#     '.#.#.': '#',
#     '.#.##': '#',
#     '.##..': '#',
#     '.####': '#',
#     '#.#.#': '#',
#     '#.###': '#',
#     '##.#.': '#',
#     '##.##': '#',
#     '###..': '#',
#     '###.#': '#',
#     '####.': '#',
# }


initial_state = "#..#.#..##......###...###"

patterns = {
    "..###": ".",
    ".##.#": "#",
    "#..#.": ".",
    "#.#.#": "#",
    "###..": "#",
    ".#..#": ".",
    "##..#": "#",
    ".###.": "#",
    "..#..": ".",
    ".....": ".",
    "#####": ".",
    ".#...": "#",
    "...#.": "#",
    "#...#": "#",
    "####.": ".",
    ".####": ".",
    "##.##": "#",
    "...##": ".",
    "..##.": ".",
    "#.##.": ".",
    "#....": ".",
    ".#.#.": ".",
    "..#.#": "#",
    "#.#..": "#",
    "##...": "#",
    "##.#.": ".",
    "#..##": ".",
    ".##..": ".",
    "#.###": ".",
    "....#": ".",
    ".#.##": "#",
    "###.#": "#",
}

initial_state = "..#..###...#####.#.#...####.#..####..###.##.#.#.##.#....#....#.####...#....###.###..##.#....#######"

state = "..." + initial_state + "..."

value = 0
res = 0
lastvalue = None
for i in range(0,300):
    lastvalue = res
    res = 0
    value = -3
    for s in state:
        if s == '#':
            res += value
        value += 1
    print(('0' if i < 10 else '') + "%s (res=%s, delta=%s): \t%s" % (i , res, res - lastvalue, state))
    state = evolve(state, patterns)

res = 0
value = -3
for s in state:
    if s == '#':
        res += value
    value += 1

print(res)

res += 53 * (50000000000 - 300)
print(res)