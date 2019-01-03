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

data = """seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
"""

ip_reg = 0

data = """addi 1 16 1
seti 1 1 3
seti 1 9 5
mulr 3 5 2
eqrr 2 4 2
addr 2 1 1
addi 1 1 1
addr 3 0 0
addi 5 1 5
gtrr 5 4 2
addr 1 2 1
seti 2 6 1
addi 3 1 3
gtrr 3 4 2
addr 2 1 1
seti 1 6 1
mulr 1 1 1
addi 4 2 4
mulr 4 4 4
mulr 1 4 4
muli 4 11 4
addi 2 6 2
mulr 2 1 2
addi 2 2 2
addr 4 2 4
addr 1 0 1
seti 0 3 1
setr 1 4 2
mulr 2 1 2
addr 1 2 2
mulr 1 2 2
muli 2 14 2
mulr 2 1 2
addr 4 2 4
seti 0 0 0
seti 0 4 1
"""

ip_reg = 1

instructions = data.splitlines()

registers = [0, 0, 0, 0, 0, 0]
ip = 0

while ip < len(instructions):
    registers[ip_reg] = ip
    debug = "ip=%s %s" % (ip, registers)
    s = instructions[ip]
    instruction, a, b, c = s.split()
    a = int(a)
    b = int(b)
    c = int(c)
    registers = opcodes[instruction](registers, a, b, c)
    debug += " %s %s" % (s, registers)
    print(debug)
    ip = registers[ip_reg] + 1

print("register #0=%s" % registers[0])
