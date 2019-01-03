from copy import deepcopy

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


def explain(line, opcode, a, b, c):
    
    if opcode == 'addr':
        print("%s\tAdd reg %s and reg %s, stores in reg %s" % (line, a,b,c))
    if opcode == 'addi':
        print("%s\tAdd reg %s and %s, stores in reg %s" % (line, a,b,c))
    if opcode == 'mulr':
        print("%s\tMultiply reg %s and reg %s, stores in reg %s" % (line, a,b,c))
    if opcode == 'muli':
        print("%s\tMultiply reg %s and %s, stores in reg %s" % (line, a,b,c))
    if opcode == 'banr':
        print("%s\treg %s & reg %s, stores in reg %s" % (line, a,b,c))
    if opcode == 'bani':
        print("%s\treg %s & %s, stores in reg %s" % (line, a,b,c))
    if opcode == 'borr':
        print("%s\treg %s | reg %s, stores in reg %s" % (line, a,b,c))
    if opcode == 'bori':
        print("%s\treg %s | %s, stores in reg %s" % (line, a,b,c))
    if opcode == 'setr':
        print("%s\tcopy reg %s to reg %s" % (line, a,c))
    if opcode == 'seti':
        print("%s\tcopy %s to reg %s" % (line, a,c))
    if opcode == 'gtir':
        print("%s\treg %s=%s > reg %s ? 1 : 0" % (line, c, a, b))
    if opcode == 'gtri':
        print("%s\treg %s=reg %s > %s ? 1 : 0" % (line, c, a, b))
    if opcode == 'gtrr':
        print("%s\treg %s=reg %s > reg %s ? 1 : 0" % (line, c, a, b))
    if opcode == 'eqir':
        print("%s\treg %s=%s == reg %s ? 1 : 0" % (line, c, a, b))
    if opcode == 'eqri':
        print("%s\treg %s=reg %s == %s ? 1 : 0" % (line, c, a, b))
    if opcode == 'eqrr':
        print("%s\treg %s=reg %s == reg %s ? 1 : 0" % (line, c, a, b))


def find_match(registers, ip_reg, instructions):
    ip = 0
    while ip < len(instructions):
        registers[ip_reg] = ip
        if ip == 16:
            print("Register #3 = %s" % registers[3])
            return registers[3]
        debug = "ip=%s %s" % (ip, registers)
        s = instructions[ip]
        instruction, a, b, c = s.split()
        a = int(a)
        b = int(b)
        c = int(c)
        registers = opcodes[instruction](registers, a, b, c)
        debug += " %s %s" % (s, registers)
        ip = registers[ip_reg] + 1


def method1(registers, ip_reg, instructions):
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
        #print(debug)
        #explain(ip, instruction, a, b, c)
        ip = registers[ip_reg] + 1


data = """
"""

ip_reg = 2

data = """seti 123 0 3
bani 3 456 3
eqri 3 72 3
addr 3 2 2
seti 0 0 2
seti 0 0 3
bori 3 65536 1
seti 4921097 0 3
bani 1 255 4
addr 3 4 3
bani 3 16777215 3
muli 3 65899 3
bani 3 16777215 3
gtir 256 1 4
addr 4 2 2
addi 2 1 2
seti 27 8 2
seti 0 5 4
addi 4 1 5
muli 5 256 5
gtrr 5 1 5
addr 5 2 2
addi 2 1 2
seti 25 1 2
addi 4 1 4
seti 17 8 2
setr 4 3 1
seti 7 9 2
eqrr 3 0 4
addr 4 2 2
seti 5 4 2"""

instructions = data.splitlines()

line = 0
for i in instructions:
    opcode, a, b, c = i.split()
    explain(line, opcode, a, b, c)
    line += 1


registers = [0, 0, 0, 0, 0, 0]

instructions = data.splitlines()
res = find_match(deepcopy(registers), ip_reg, instructions)
registers[0] = res
method1(deepcopy(registers), ip_reg, instructions)
