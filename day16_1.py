def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]
    return regs


def addi(regs, a, b, c):
    regs[c] = regs[a] + b
    return regs


def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]
    return regs


def muli(regs, a, b, c):
    regs[c] = regs[a] * b
    return regs


def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]
    return regs


def bani(regs, a, b, c):
    regs[c] = regs[a] & b
    return regs


def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]
    return regs


def bori(regs, a, b, c):
    regs[c] = regs[a] | b
    return regs


def setr(regs, a, b, c):
    regs[c] = regs[a]
    return regs


def seti(regs, a, b, c):
    regs[c] = a
    return regs


def gtir(regs, a, b, c):
    regs[c] = 1 if a > regs[b] else 0
    return regs


def gtri(regs, a, b, c):
    regs[c] = 1 if regs[a] > b else 0
    return regs


def gtrr(regs, a, b, c):
    regs[c] = 1 if regs[a] > regs[b] else 0
    return regs


def eqir(regs, a, b, c):
    regs[c] = 1 if a == regs[b] else 0
    return regs


def eqri(regs, a, b, c):
    regs[c] = 1 if regs[a] == b else 0
    return regs


def eqrr(regs, a, b, c):
    regs[c] = 1 if regs[a] == regs[b] else 0
    return regs


opcodes = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}


def test_opcode(before, after, opcode, a, b, c):
    res = 0
    for opcode, f in opcodes.items():
        rregs = f(before.copy(), a, b, c)
        if rregs[0] == after[0] and rregs[1] == after[1] and rregs[2] == after[2] and rregs[3] == after[3]:
            res += 1

    return res

test_opcode([3,2,1,1], [3,2,2,1], 9,2,1,2)

total_count = 0

if test_opcode([0, 2, 2, 2], [0, 2, 2, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 2, 1, 1], [3, 2, 1, 0], 11, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 1], [1, 2, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 2], [1, 0, 0, 2], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 3], [3, 2, 3, 0], 10, 1, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [1, 1, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [1, 1, 2, 0], 6, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 1], [0, 1, 3, 1], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 1, 3], [1, 0, 1, 3], 10, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([3, 3, 0, 2], [1, 3, 0, 2], 3, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 0], [2, 1, 0, 0], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 2], [1, 3, 3, 2], 7, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 1], [1, 0, 2, 1], 12, 0, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 0], [0, 1, 0, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 2, 1], 0, 0, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 0], [0, 2, 1, 0], 0, 0, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 2], [3, 1, 3, 2], 7, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 2], [1, 3, 1, 2], 7, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 3], [0, 3, 0, 3], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 3], [0, 1, 1, 3], 0, 0, 3, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [1, 0, 2, 3], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 2], [3, 1, 3, 2], 7, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [1, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 1], [1, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 1, 1], [2, 1, 1, 1], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 0], [1, 0, 2, 0], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 1], [2, 3, 1, 1], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 2], [3, 3, 2, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 3], [0, 1, 3, 1], 8, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 0], [0, 3, 2, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 2], [0, 3, 0, 2], 0, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [3, 0, 3, 3], 10, 1, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 1, 1], [1, 1, 0, 1], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 1], [0, 0, 1, 1], 0, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 0, 3], [1, 0, 1, 3], 12, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 2], [2, 0, 3, 2], 15, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 1], [1, 0, 1, 1], 12, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 0, 2], [3, 1, 0, 1], 3, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 3], [0, 2, 0, 3], 0, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 0, 2], [3, 2, 0, 1], 3, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 0], [2, 0, 0, 0], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [1, 0, 2, 1], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 3], [1, 3, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 3], [0, 2, 2, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 0], [1, 0, 2, 0], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 2], [2, 0, 1, 2], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 2], [1, 3, 3, 2], 7, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 1], [1, 3, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 2], [0, 1, 2, 2], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [3, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 3], [0, 2, 2, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 1], [3, 3, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 3], [0, 1, 0, 3], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 1, 0, 3], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 0, 3], [3, 3, 0, 1], 8, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 3], [2, 1, 0, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 1], [3, 1, 0, 1], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 0, 2], [3, 3, 0, 1], 3, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 0, 1], [2, 2, 0, 1], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 0], [0, 1, 2, 0], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 1, 3], [3, 0, 1, 3], 10, 1, 3, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 1, 0, 3], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 3], [3, 2, 2, 3], 15, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 0], [1, 1, 3, 0], 3, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 3], [3, 1, 3, 3], 8, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 1], [0, 1, 1, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 2], [3, 0, 1, 2], 3, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 2], [0, 0, 2, 2], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 1, 0, 1], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 3], [0, 1, 0, 3], 0, 0, 3, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 1, 3], [3, 1, 1, 3], 8, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [3, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 0, 3, 2], 6, 2, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 3, 2, 3], [2, 3, 2, 1], 8, 2, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 3], [0, 0, 1, 0], 0, 0, 1, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [1, 1, 2, 1], 8, 2, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 3], [1, 0, 3, 1], 12, 0, 1, 3) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 1], [3, 2, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 2], [3, 1, 2, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 1], [2, 1, 2, 1], 8, 2, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 0], [0, 3, 2, 0], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 2], [2, 3, 3, 2], 15, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 3], [2, 0, 2, 3], 10, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 2], [0, 3, 1, 2], 7, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 2], [3, 0, 1, 2], 7, 3, 0, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 3], [1, 0, 2, 3], 10, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 2], [0, 0, 3, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 1], [1, 0, 1, 1], 12, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 1], [1, 0, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 2], [1, 3, 2, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 0], [2, 2, 3, 0], 15, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 2], [2, 3, 2, 2], 15, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 0, 3], [3, 1, 0, 3], 8, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 3], [0, 2, 2, 3], 6, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [3, 0, 2, 3], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [2, 1, 2, 0], 8, 2, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [1, 1, 0, 3], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 2], [0, 0, 1, 2], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 3], [0, 0, 0, 3], 10, 1, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 0], [1, 0, 2, 0], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 3], [2, 0, 2, 0], 10, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 1], [0, 3, 0, 1], 0, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 3], [1, 3, 0, 3], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 1], [1, 2, 1, 1], 6, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [0, 1, 2, 1], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 0], [0, 1, 2, 0], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 1], [0, 0, 3, 1], 11, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 1], [3, 1, 2, 1], 12, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 1], [3, 1, 0, 1], 12, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 1], [3, 0, 1, 1], 12, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 1], [1, 0, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 0], [0, 1, 1, 0], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 0], [1, 2, 1, 0], 6, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 1], [2, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 3], [3, 3, 2, 3], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 1], [0, 0, 1, 1], 12, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 0], [1, 0, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 2], [1, 0, 1, 1], 12, 2, 1, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 3], [0, 1, 1, 0], 10, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 0, 2], [1, 3, 0, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 0, 1], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [0, 1, 3, 3], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [2, 0, 3, 3], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 2, 1, 1], [3, 0, 1, 1], 11, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 0], [0, 0, 2, 0], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 2, 0, 3], [2, 2, 0, 1], 6, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 2], [2, 0, 2, 2], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 2], [2, 1, 3, 2], 15, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 2], [0, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 3], [1, 3, 0, 3], 10, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 0], [1, 2, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 1], [0, 2, 2, 1], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 3, 2, 1], [2, 3, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 0, 2], [1, 0, 1, 2], 3, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 2], [2, 1, 0, 1], 3, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 2], [0, 2, 3, 2], 15, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 0], [3, 0, 1, 0], 3, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 1], [0, 0, 2, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 1], [0, 0, 0, 1], 0, 0, 3, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 3], [2, 0, 0, 3], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 2, 1, 3], [2, 2, 1, 3], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 3], [0, 0, 2, 3], 10, 1, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 1, 0], [1, 1, 2, 0], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 2, 1], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 3, 2, 1], [2, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 2], [1, 2, 3, 2], 15, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 3], [3, 2, 2, 1], 8, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 3], [2, 2, 2, 0], 10, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 3], [0, 0, 1, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 1], [0, 0, 2, 1], 0, 0, 3, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 3], [0, 2, 2, 3], 10, 1, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 3], [0, 1, 2, 3], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 3], [0, 0, 2, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 1], [3, 2, 0, 1], 8, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 1], [0, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 1], [2, 2, 3, 1], 15, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 1, 0, 3], 6, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 3], [0, 0, 3, 3], 0, 0, 1, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 2], [0, 0, 0, 2], 0, 0, 3, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 3], [2, 0, 1, 3], 10, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [1, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 1], [2, 0, 3, 1], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 0], [1, 0, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 2], [0, 1, 0, 2], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 0, 2], [1, 2, 0, 2], 3, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 1], [2, 1, 0, 1], 11, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 3, 3, 2], [1, 3, 2, 2], 15, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 3], [0, 2, 3, 3], 10, 1, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 2], [0, 0, 3, 2], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 1, 0, 3], 6, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 3], [0, 2, 1, 1], 6, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [1, 2, 2, 1], 8, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 3], [0, 2, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 0], [0, 3, 0, 0], 0, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 0], [1, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 2], [1, 0, 1, 2], 12, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 3], [0, 3, 3, 3], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 1], [0, 0, 2, 1], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 2], [2, 0, 3, 2], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [0, 2, 2, 1], 8, 2, 1, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 0], [0, 1, 1, 0], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 0], [1, 1, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 1], [0, 3, 0, 1], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 1], [0, 0, 3, 1], 8, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [3, 1, 2, 3], 8, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 0, 1], 0, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [0, 1, 2, 1], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 0], [2, 3, 1, 0], 3, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 3], [0, 0, 2, 3], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 0], [3, 3, 1, 2], 1, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 0], [3, 0, 2, 0], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 0], [0, 1, 0, 0], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 1], [2, 0, 0, 1], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 0], [1, 0, 1, 0], 12, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 0, 2], [2, 0, 1, 2], 3, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 1], [2, 2, 3, 1], 15, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 0], [0, 0, 1, 0], 0, 0, 1, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 1, 3], [1, 1, 0, 3], 10, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 0], [0, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 0], [2, 3, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 2], [3, 0, 3, 2], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 3], [0, 1, 1, 2], 1, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 1], [2, 0, 3, 1], 8, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 0], [0, 1, 1, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 1], [1, 2, 2, 1], 15, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 2], [1, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 1], [1, 0, 2, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 1], [1, 0, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 2], [0, 1, 2, 2], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 1, 2], [1, 3, 0, 2], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 2], [1, 1, 2, 2], 12, 0, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 0], [0, 1, 3, 0], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 1], [2, 2, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 2], [1, 2, 3, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 1], [1, 2, 3, 0], 8, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 0, 2], [3, 3, 0, 1], 7, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 0], [0, 0, 1, 0], 3, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 2], [1, 2, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 1, 3], [0, 1, 1, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 0], [1, 1, 0, 0], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 3], [0, 0, 0, 3], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 1], [0, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 3], [2, 0, 0, 3], 10, 1, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 3], [0, 0, 1, 3], 8, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 0, 2, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 2], [1, 1, 2, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 1], [0, 2, 0, 1], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [2, 1, 2, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 1], [2, 2, 3, 1], 15, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 2], [2, 0, 3, 2], 15, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 3, 1, 2], [1, 3, 1, 2], 7, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [0, 1, 2, 1], 11, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 1], [0, 3, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 1], [0, 1, 0, 1], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 0], [3, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 3], [0, 1, 0, 3], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 1], [2, 1, 1, 1], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 2], [2, 2, 1, 2], 1, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 0], [0, 2, 2, 1], 6, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 0], [0, 3, 3, 0], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 1, 0, 2], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 1], [0, 0, 1, 1], 12, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [2, 1, 2, 3], 15, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 1, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [2, 0, 2, 0], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 1], [0, 2, 0, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 0], [0, 2, 2, 0], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 1], [0, 0, 2, 1], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 1], [1, 2, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [0, 1, 2, 3], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 2], [1, 3, 2, 2], 7, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 0], [0, 1, 3, 0], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 1], [2, 1, 0, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 0], [2, 2, 3, 0], 15, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 2], [3, 0, 0, 1], 3, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 0], [3, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 0, 2, 1], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 3], [1, 1, 2, 3], 6, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 1], [0, 1, 1, 1], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 2], [0, 1, 1, 2], 0, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 1], [3, 0, 1, 1], 12, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 3], [0, 0, 1, 3], 0, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [1, 1, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 2], [1, 1, 2, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 1, 1, 0], 3, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 0], [1, 2, 3, 2], 15, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 3], [1, 0, 1, 3], 12, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 3], [3, 3, 1, 1], 8, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [0, 2, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 1], [1, 3, 0, 1], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 0], [3, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 1], [0, 0, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [1, 0, 2, 3], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [0, 1, 2, 3], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 1, 2, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 3], [0, 0, 1, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 2, 1, 1], [2, 2, 1, 1], 1, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [2, 1, 0, 3], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 3], [0, 2, 2, 3], 0, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [0, 1, 2, 3], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 1, 3, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 3], [0, 3, 0, 3], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 0], [2, 0, 2, 0], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 2], [1, 0, 3, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 2], [1, 1, 2, 2], 6, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 3], [0, 2, 0, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 1], [2, 0, 1, 1], 12, 2, 1, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 2], [2, 1, 0, 2], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 2], [0, 0, 2, 2], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 2], [2, 0, 3, 2], 15, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [0, 1, 3, 3], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 2], [1, 0, 2, 2], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 1, 3], [1, 2, 1, 0], 10, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [0, 1, 2, 1], 8, 2, 1, 1) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 1], [0, 3, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 1], [3, 0, 2, 1], 12, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 3, 2], [1, 3, 3, 2], 15, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 3, 0, 2], [2, 3, 1, 2], 3, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 2], [3, 3, 1, 2], 6, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 2], [1, 3, 2, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 2], [2, 1, 0, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 2], [1, 0, 2, 2], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 3], [0, 0, 0, 3], 0, 0, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 3], [0, 1, 1, 3], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 1], [1, 0, 1, 1], 12, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [2, 0, 2, 0], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [3, 1, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 0], [2, 0, 1, 0], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [2, 1, 3, 0], 10, 1, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 0, 1], [1, 0, 0, 1], 12, 0, 1, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 3], [3, 0, 1, 1], 12, 2, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 1], [1, 0, 3, 1], 8, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 3], [0, 2, 2, 3], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 3], [0, 0, 1, 3], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [0, 2, 2, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 2], [2, 1, 0, 2], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 1], [0, 0, 3, 1], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 0], [1, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 2, 0, 1], [3, 2, 0, 1], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 2], [2, 2, 3, 2], 15, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 3], [0, 3, 2, 3], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 3], [1, 2, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 2], [1, 0, 2, 2], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 3], [1, 3, 1, 3], 8, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 3, 3], [1, 3, 3, 3], 8, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 2], [3, 1, 2, 2], 7, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 3], [1, 2, 2, 3], 15, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 0], [3, 1, 0, 0], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 1], [2, 2, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 2], [0, 1, 0, 2], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 3], [0, 2, 0, 3], 0, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 1], [0, 0, 1, 1], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [0, 1, 2, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 1], [3, 0, 3, 1], 12, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 2], [1, 3, 2, 1], 7, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 0], [0, 2, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 1, 2], [3, 1, 1, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 3], [1, 0, 2, 3], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 0], [1, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 3], [3, 0, 1, 0], 10, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 1], [2, 0, 1, 1], 12, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 2], [3, 0, 3, 2], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 0], [0, 3, 2, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 3], [1, 0, 1, 3], 12, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 3], [0, 3, 1, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 0], [3, 3, 2, 1], 6, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 0], [1, 1, 2, 0], 8, 2, 1, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 2], [0, 1, 3, 2], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 0, 2, 3], 10, 1, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 0], [1, 3, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 2], [0, 2, 3, 2], 15, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 0, 2], [1, 1, 0, 2], 3, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 0], [3, 0, 2, 0], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 2], [1, 0, 2, 2], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 3, 0], [1, 3, 3, 0], 3, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 2], [0, 1, 0, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [3, 1, 0, 3], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 1, 3], [3, 0, 1, 3], 10, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 2], [1, 1, 0, 2], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 3], [1, 2, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 2], [0, 1, 1, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 1], [3, 0, 3, 1], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 3], [2, 1, 2, 3], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 0], [0, 1, 1, 2], 1, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 3], [0, 1, 3, 3], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 1, 2], [1, 3, 1, 1], 7, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 2], [1, 0, 3, 2], 12, 0, 1, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 0], [2, 0, 3, 0], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 3], [2, 1, 0, 3], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 3], [2, 2, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 1, 3, 2], 15, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 1], [2, 1, 0, 1], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 1], [3, 0, 0, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 3], [1, 0, 2, 3], 6, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [1, 0, 2, 1], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 0], [0, 1, 0, 0], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 3], [0, 1, 0, 3], 6, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 0, 2], [1, 1, 0, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 2, 1, 2], [2, 2, 0, 2], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [0, 1, 2, 1], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 2], [0, 0, 0, 2], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [2, 1, 3, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 0, 3], [2, 2, 0, 0], 10, 1, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [2, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 0], [1, 0, 2, 0], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 0, 2, 3], 6, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 2], [0, 0, 3, 2], 0, 0, 1, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 1, 0, 0], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 1], [0, 1, 0, 1], 0, 0, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 2], [0, 2, 2, 2], 15, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 2], [3, 0, 1, 1], 7, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 1, 2], [3, 1, 1, 2], 7, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [1, 1, 2, 0], 8, 2, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 0], [2, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 0], [0, 3, 0, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 1, 2], [3, 1, 2, 2], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 0], [0, 0, 1, 0], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [0, 2, 2, 1], 11, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 3, 1, 2], [2, 3, 1, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 2], [3, 3, 1, 2], 7, 3, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 1, 2, 2], 15, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 1, 2], [3, 1, 1, 1], 7, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 1], [0, 0, 3, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 1], [1, 3, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 0], [2, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 0, 1], [1, 0, 0, 1], 12, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 1], [1, 3, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 1], [0, 3, 2, 1], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 1, 2], [1, 1, 1, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 1], [2, 0, 2, 1], 12, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 0], [3, 0, 1, 2], 1, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 0, 2], [1, 3, 0, 2], 7, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 1], [0, 0, 3, 1], 8, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 1], [2, 0, 3, 2], 15, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 1], [0, 0, 0, 1], 0, 0, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 3], [0, 3, 2, 3], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 3], [0, 1, 1, 3], 10, 1, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 2], [0, 0, 1, 2], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 1], [3, 2, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 2], [3, 3, 1, 2], 7, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 2], [0, 2, 2, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 0, 2, 1], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 2], [3, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 2], [1, 0, 1, 2], 12, 0, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 0], [0, 0, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [1, 1, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 1], [3, 0, 1, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 0, 2], [1, 0, 0, 1], 12, 0, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 1, 3], [1, 2, 2, 3], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 1], [3, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 1], [0, 0, 0, 0], 0, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [3, 0, 3, 3], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 1, 0], [1, 2, 2, 0], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 1], [0, 3, 2, 1], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 1], [0, 3, 3, 1], 8, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [0, 1, 2, 0], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 2], [2, 0, 1, 2], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 1, 3], [1, 1, 1, 0], 10, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 0], [1, 0, 1, 0], 12, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 1, 2], [3, 2, 1, 1], 7, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 2], [1, 1, 3, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 2], [0, 3, 2, 2], 15, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 0], [0, 0, 0, 0], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 0], [0, 1, 3, 0], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 3], [0, 1, 3, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 2], [2, 0, 1, 2], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 3], [1, 2, 3, 1], 8, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 2], [3, 2, 3, 2], 15, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 0, 3, 0], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 1], [2, 0, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 0, 3], [3, 2, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 2], [2, 3, 1, 2], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [0, 1, 2, 3], 6, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 3], [0, 2, 2, 1], 6, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 2], [1, 3, 3, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 2], [0, 1, 1, 1], 6, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 0], [0, 0, 3, 0], 0, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 2], [3, 1, 0, 2], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 1, 1], [1, 1, 2, 1], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 2], [1, 1, 0, 2], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 1], [2, 1, 0, 1], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 1], [1, 2, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [1, 1, 0, 3], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 1], [0, 1, 2, 1], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 1], [0, 2, 3, 1], 6, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 2], [2, 2, 3, 2], 15, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 1], [2, 1, 0, 1], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 1], [0, 1, 3, 1], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [0, 1, 3, 3], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 3], [1, 0, 2, 3], 12, 0, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 3], [1, 0, 2, 3], 8, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 1], [1, 0, 1, 1], 12, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 0], [0, 0, 0, 0], 0, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 2], [0, 1, 1, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 2], [2, 1, 0, 2], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 1], [0, 2, 3, 1], 0, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 1], [3, 1, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 2], [3, 3, 1, 2], 7, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 1], [0, 1, 0, 1], 0, 0, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 3], [2, 0, 2, 3], 10, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 3], [0, 2, 1, 3], 1, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 1], [3, 2, 2, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 3], [0, 1, 0, 3], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 2], [2, 0, 2, 1], 8, 2, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 1], [1, 0, 1, 1], 12, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 3], [3, 2, 0, 3], 10, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 2], [1, 2, 3, 2], 15, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 1, 2], [1, 3, 1, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 1], [3, 0, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 2], [2, 0, 1, 1], 12, 2, 1, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [2, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 2], [2, 1, 0, 2], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 0], [0, 2, 2, 0], 0, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 1], [1, 2, 2, 1], 6, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 1], [1, 3, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 1], [1, 2, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [3, 1, 3, 0], 10, 1, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 3], [0, 0, 1, 3], 0, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 3], [3, 0, 3, 1], 6, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 3, 2], [1, 1, 3, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 1], [2, 0, 3, 1], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 3], [3, 2, 2, 0], 10, 1, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 1], [2, 1, 3, 1], 12, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 3], [0, 2, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 3, 1, 3], [0, 3, 1, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [0, 1, 2, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [2, 1, 0, 0], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 3], [2, 3, 3, 3], 15, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 3], [2, 2, 2, 3], 15, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 2], [1, 3, 1, 2], 7, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 3], [1, 1, 1, 3], 6, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 1], [0, 0, 1, 1], 11, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 1, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 2], [0, 1, 0, 2], 3, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 3], [0, 0, 1, 3], 10, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 1], [0, 3, 0, 1], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 1], [3, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 1], [0, 1, 0, 1], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 2], [2, 3, 1, 2], 7, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [1, 1, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 1], [2, 0, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 1], [3, 0, 1, 1], 12, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 1], [3, 0, 1, 1], 12, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 0], [3, 2, 1, 0], 1, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 1], [3, 0, 2, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 3], [2, 0, 1, 3], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 3], [0, 0, 2, 3], 0, 0, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [1, 1, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 1], [0, 1, 3, 1], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 3], [1, 0, 1, 2], 1, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 1], [1, 0, 2, 1], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 2], [3, 0, 2, 2], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 2], [0, 2, 3, 2], 15, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 1], [2, 1, 0, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 3], [0, 0, 2, 1], 6, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([1, 3, 0, 2], [1, 3, 1, 2], 3, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 0], [2, 1, 1, 0], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 2], [1, 2, 0, 2], 6, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [3, 1, 3, 1], 8, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 0, 3, 2], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 2], [2, 1, 1, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 1], [0, 0, 2, 1], 12, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 3], [1, 0, 1, 3], 12, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 3], [2, 0, 2, 3], 6, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 3], [1, 2, 0, 3], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [2, 1, 0, 0], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 2], [0, 2, 0, 2], 0, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 3], [1, 0, 0, 3], 10, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 3], [1, 1, 0, 3], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 2], [2, 2, 2, 2], 15, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 1], [0, 0, 1, 1], 6, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 0, 2], [1, 1, 0, 2], 3, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 2], [0, 1, 0, 2], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 0], [1, 0, 3, 0], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 3, 2], [1, 2, 3, 2], 15, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 1, 1], [1, 2, 2, 1], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 2], [1, 3, 1, 2], 6, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 1], [0, 3, 3, 0], 8, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 3], [3, 2, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 1], [1, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 1], [2, 1, 2, 1], 6, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 1], [1, 0, 2, 1], 14, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 1], [0, 0, 0, 1], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 0, 2, 1], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 0], [0, 2, 1, 0], 8, 2, 1, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 3], [3, 0, 1, 3], 8, 3, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 0, 2, 1], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 1, 3], [1, 0, 1, 3], 6, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 2], [3, 1, 0, 2], 7, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 3], [2, 1, 0, 3], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 2], [0, 2, 1, 2], 1, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 1], [2, 2, 1, 1], 1, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 0], [0, 1, 2, 0], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 0, 2, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 0], [1, 0, 1, 0], 12, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 3], [2, 1, 0, 0], 10, 1, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 3], [0, 2, 2, 3], 10, 1, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 2], [0, 0, 2, 2], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 1], [0, 2, 2, 1], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 0, 2], [1, 2, 0, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 0, 2], [3, 3, 0, 1], 7, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 2], [1, 1, 0, 2], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 3], [3, 2, 1, 3], 6, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 0], [1, 0, 3, 0], 3, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 3, 0, 1], [2, 3, 0, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 1, 3], [0, 1, 1, 3], 6, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [0, 1, 3, 2], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 2], [0, 1, 0, 2], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 1], [1, 1, 1, 1], 12, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 0, 1], [2, 0, 0, 1], 12, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 2], [3, 1, 2, 2], 15, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 3], [2, 2, 2, 3], 15, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 3], [0, 0, 1, 3], 6, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 2], [3, 0, 2, 2], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 1], [2, 0, 3, 1], 15, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 0], [3, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 2], [2, 1, 2, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 0], [2, 0, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 0, 2], [1, 1, 0, 2], 3, 2, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 1], [0, 0, 0, 1], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 1, 0], [3, 0, 1, 1], 12, 2, 1, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 1], [2, 0, 0, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 0], [0, 1, 2, 0], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [0, 2, 2, 1], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 0], [3, 2, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 1, 3, 0], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 2], [3, 0, 3, 2], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 3], [0, 2, 2, 3], 10, 1, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [2, 0, 3, 3], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 1], [1, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 2], [0, 1, 2, 2], 11, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 2], [0, 1, 0, 2], 3, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 0], [0, 0, 2, 0], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 2, 1, 1], [2, 2, 1, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 0], [0, 2, 1, 0], 0, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 3], [1, 3, 3, 3], 6, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 2], [1, 2, 3, 2], 15, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 3], [2, 0, 2, 3], 10, 1, 3, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 2], [0, 1, 2, 2], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 1, 3], [1, 1, 1, 3], 8, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 1], [3, 2, 2, 1], 15, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 1, 0, 3], 10, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 3, 1, 0], [2, 3, 2, 0], 1, 2, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 2], [0, 1, 0, 2], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 1], [0, 2, 0, 1], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 1], [0, 1, 3, 1], 6, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 1, 2], [1, 3, 1, 2], 7, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 3], [0, 3, 1, 0], 10, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 1, 0], [2, 0, 1, 0], 12, 2, 1, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [1, 1, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 0], [1, 3, 0, 0], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 3], [0, 1, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 1], [1, 0, 1, 1], 5, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 0], [2, 1, 0, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 2], [0, 0, 2, 2], 0, 0, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 0], [0, 1, 0, 0], 0, 0, 1, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 2], [0, 2, 2, 2], 15, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [0, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 0], [0, 2, 2, 0], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 0], [3, 1, 0, 0], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 0], [1, 0, 3, 0], 3, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 2], [1, 3, 2, 2], 6, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 0], [2, 2, 3, 0], 15, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 0], [1, 1, 3, 0], 3, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 1], [1, 0, 2, 1], 12, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 0, 1], [0, 0, 0, 1], 0, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 1], [0, 0, 3, 1], 12, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [1, 1, 3, 3], 8, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 1], [2, 1, 0, 1], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 3], [0, 3, 1, 3], 9, 0, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 1, 2], [2, 2, 1, 2], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 2], [0, 1, 2, 2], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 0, 3], [0, 2, 0, 3], 10, 1, 3, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 0, 2], [1, 2, 0, 2], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 1, 1], [0, 1, 0, 1], 11, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [3, 1, 0, 3], 10, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 0], [0, 3, 0, 0], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 1], [0, 1, 3, 1], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 3], [2, 2, 3, 3], 15, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 0], [0, 0, 2, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 0], [2, 1, 0, 0], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 2], [0, 3, 1, 2], 7, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 0], [0, 3, 0, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 1], [3, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 3], [2, 1, 1, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [2, 1, 2, 1], 8, 2, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 2], [0, 3, 1, 2], 6, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 2], [1, 0, 1, 2], 1, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 2], [3, 1, 3, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 0, 2, 3], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 1], [1, 2, 3, 0], 11, 3, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 1], [1, 0, 2, 1], 11, 3, 3, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 0, 3, 0], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 2], [3, 0, 2, 1], 7, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 2], [2, 0, 3, 2], 15, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 3], [3, 1, 3, 3], 8, 3, 0, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 2], [0, 0, 2, 2], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 2], [2, 0, 0, 2], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 0], [2, 0, 2, 0], 15, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 3], [2, 2, 1, 3], 8, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [1, 1, 0, 1], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 2], [2, 2, 3, 2], 15, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 0], [1, 2, 2, 0], 8, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 0, 2], [3, 2, 0, 1], 7, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 3, 1, 0], [0, 3, 1, 0], 0, 0, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 2], [1, 0, 0, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 0, 2], [3, 3, 1, 2], 3, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 0, 2, 0], [2, 0, 1, 0], 8, 2, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 0], [2, 1, 0, 0], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 3], [0, 1, 2, 3], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 2, 3, 2], 15, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 2, 0, 2], [3, 2, 1, 2], 7, 3, 0, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 2], [1, 2, 0, 2], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 1], [0, 1, 3, 1], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 3, 2], [1, 3, 3, 1], 7, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 0, 0, 2], [1, 0, 1, 2], 12, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 3], [0, 0, 1, 3], 6, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 2], [0, 1, 3, 2], 13, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 3, 2, 2], [1, 3, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 0], [2, 2, 1, 0], 3, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 0], [3, 0, 3, 0], 13, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 2], [0, 1, 1, 2], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 3], [0, 2, 3, 1], 8, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 1], [0, 2, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 3], [0, 2, 2, 0], 10, 1, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [0, 1, 2, 1], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 1], [2, 1, 0, 1], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 0], [0, 3, 0, 0], 0, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([2, 3, 1, 1], [2, 3, 1, 1], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 3], [2, 1, 2, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 2], [1, 2, 2, 2], 8, 2, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 0, 0, 1], [1, 0, 0, 1], 12, 0, 1, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 1, 0, 2], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 3], [0, 1, 2, 3], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 2, 1, 1], [2, 2, 1, 1], 1, 2, 2, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 2], [3, 1, 1, 2], 7, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 2], [3, 3, 1, 2], 1, 2, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 0], [0, 0, 2, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 1], [1, 1, 0, 1], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 0], [1, 0, 3, 0], 3, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 0], [2, 2, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 2], [0, 1, 0, 2], 3, 2, 3, 1) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [0, 1, 2, 3], 2, 1, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 3], [0, 1, 3, 3], 8, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 0], [0, 1, 3, 0], 3, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 1], [3, 0, 1, 1], 12, 3, 1, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 2], [3, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 0], [0, 1, 2, 0], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 3, 2], [3, 3, 2, 2], 15, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 3, 2], [1, 0, 3, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 0, 2, 1], [3, 0, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 2], [2, 2, 3, 2], 15, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 2, 2, 2], [0, 2, 2, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [3, 1, 3, 1], 8, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 1, 3], [0, 1, 1, 3], 12, 2, 1, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 1, 3], [1, 0, 1, 3], 12, 2, 1, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 2], [2, 1, 2, 0], 2, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 1], [2, 1, 3, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 3], [3, 1, 0, 3], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 3], [1, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([2, 2, 3, 1], [2, 2, 3, 2], 15, 1, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 2], [0, 1, 2, 2], 11, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 3], [3, 1, 1, 3], 8, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 3], [0, 3, 3, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 3], [0, 0, 2, 3], 2, 1, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 3], [0, 1, 0, 3], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 2, 3, 1], [3, 2, 0, 1], 11, 3, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 3, 3], [0, 2, 1, 3], 8, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 0], [3, 1, 1, 0], 3, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 0, 0, 2], [3, 0, 0, 1], 7, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 3], [0, 0, 3, 3], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 2, 1], [2, 1, 0, 1], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 2], [2, 1, 0, 2], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 3, 3], [0, 3, 3, 1], 8, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 0, 3], [1, 2, 0, 3], 10, 1, 3, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 2], [0, 2, 2, 2], 14, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 2, 2], [0, 3, 2, 1], 7, 3, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 1], [1, 1, 2, 1], 5, 3, 2, 0) >= 3:
    total_count += 1

if test_opcode([1, 2, 1, 1], [0, 2, 1, 1], 11, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 1], [0, 1, 0, 1], 4, 1, 0, 0) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 3], [3, 2, 2, 1], 8, 2, 1, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 2, 2], [3, 1, 2, 1], 7, 3, 0, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 3], [2, 2, 1, 3], 1, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 0], [0, 0, 0, 0], 0, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 1], [0, 3, 0, 1], 0, 0, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 1, 3], [0, 0, 1, 3], 0, 0, 3, 1) >= 3:
    total_count += 1

if test_opcode([1, 3, 3, 0], [1, 3, 3, 1], 3, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 1], [0, 0, 0, 1], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 1], [0, 1, 2, 1], 12, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 2], [0, 1, 0, 2], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([2, 0, 3, 2], [2, 0, 3, 2], 15, 0, 2, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 2, 0], 0, 0, 1, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 0], [1, 2, 0, 0], 14, 0, 2, 2) >= 3:
    total_count += 1

if test_opcode([0, 2, 0, 3], [0, 2, 0, 3], 9, 0, 0, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 3], [1, 0, 2, 3], 6, 3, 1, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 2, 0], [1, 1, 2, 0], 6, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 2, 1], [0, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 1], [0, 0, 0, 1], 0, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 1], [3, 1, 2, 1], 6, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 0, 3, 0], [1, 0, 1, 0], 3, 3, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 2, 2, 0], [1, 2, 2, 0], 14, 0, 2, 3) >= 3:
    total_count += 1

if test_opcode([3, 2, 2, 2], [1, 2, 2, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 1, 0, 0], 13, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 1], [1, 1, 0, 1], 8, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 1], [2, 1, 1, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 2, 1], [0, 1, 2, 1], 5, 3, 2, 3) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 3], [1, 1, 0, 3], 6, 3, 3, 0) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 1], [1, 0, 3, 1], 12, 3, 1, 0) >= 3:
    total_count += 1

if test_opcode([0, 3, 0, 2], [0, 0, 0, 2], 9, 0, 0, 1) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 1], [2, 1, 2, 1], 5, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 3, 3, 1], [2, 2, 3, 1], 15, 0, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 2, 2, 2], [2, 2, 2, 1], 8, 2, 0, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 1], [1, 2, 0, 1], 8, 2, 3, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 3, 0], [0, 1, 3, 0], 9, 0, 0, 3) >= 3:
    total_count += 1

if test_opcode([1, 2, 3, 2], [1, 2, 3, 2], 15, 3, 2, 1) >= 3:
    total_count += 1

if test_opcode([1, 1, 2, 0], [1, 1, 0, 0], 2, 1, 2, 2) >= 3:
    total_count += 1

if test_opcode([3, 1, 1, 3], [3, 0, 1, 3], 10, 1, 3, 1) >= 3:
    total_count += 1

if test_opcode([3, 3, 2, 3], [3, 3, 2, 0], 10, 2, 3, 3) >= 3:
    total_count += 1

if test_opcode([2, 1, 3, 3], [2, 1, 0, 3], 4, 1, 0, 2) >= 3:
    total_count += 1

if test_opcode([0, 1, 0, 2], [0, 1, 0, 2], 0, 0, 1, 2) >= 3:
    total_count += 1

if test_opcode([2, 1, 1, 0], [2, 1, 1, 0], 4, 1, 0, 3) >= 3:
    total_count += 1

if test_opcode([3, 2, 1, 0], [3, 2, 1, 0], 1, 2, 2, 1) >= 3:
    total_count += 1

if test_opcode([2, 1, 0, 2], [2, 0, 0, 2], 4, 1, 0, 1) >= 3:
    total_count += 1

if test_opcode([0, 0, 3, 3], [0, 0, 3, 0], 0, 0, 3, 3) >= 3:
    total_count += 1

if test_opcode([3, 1, 3, 2], [0, 1, 3, 2], 6, 2, 1, 0) >= 3:
    total_count += 1

if test_opcode([3, 3, 1, 2], [1, 3, 1, 2], 7, 3, 0, 0) >= 3:
    total_count += 1

if test_opcode([1, 1, 3, 2], [1, 1, 3, 0], 13, 1, 2, 3) >= 3:
    total_count += 1

print(total_count)
