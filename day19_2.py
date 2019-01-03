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


def method1(registers, ip_reg, instructions):
    ip = 1

    while ip < len(instructions):
        registers[ip_reg] = ip
        # if ip == 3:
        #      print("!!! new loop ! registers : %s" % registers)
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

    print("register #0=%s" % registers[0])


def method2(registers, ip_reg, instructions):
    # 1
    registers[3] = 1
    # 2
    registers[5] = 1

    while True:
        # print("!!! new loop ! registers : %s" % registers)
        # 3
        registers[2] = registers[3] * registers[5]
        # 4
        registers[2] = 1 if registers[2] == registers[4] else 0
        # 5
        if registers[2] == 1:
            # 7
            registers[0] += registers[3]
        # 6+8
        registers[5] += 1
        # 9
        registers[2] = 1 if registers[5] > registers[4] else 0
        # 10
        if registers[2] == 1:
            # 12
            registers[3] += 1
            # 13
            registers[2] = 1 if registers[3] > registers[4] else 0
            # 14
            if registers[2] == 1:
                # 16
                print(registers[0])
                return
            # 2
            registers[5] = 1
    """
    1 #3 = 1

2 #5 = 1

3 #2 = #3*#5
4 #2 = 1 if #2 == #4 else 0
5 jump to 7 if #2 == 1
6 jump to 8 if #2 == 0
7 #0 += #3
8 #5 += 1
9 #2 = 1 if #5 > #4 else 0
10 jump to 12 if #2 == 1
11 jump to 3
12 #3 += 1
13 #2 = 1 if #3 > #4
14 jump to 16 if #2 == 1
15 jump to 2
16 jump to 256 (halt)
    """


def method3(registers, ip_reg, instructions):
    # 1
    registers[3] = 1
    # 2
    registers[5] = 1

    while True:
        # print("!!! new loop ! registers : %s" % registers)
        # 3, 4, 5, 7
        if registers[3] * registers[5] == registers[4]:
            registers[0] += registers[3]
        # 6+8
        registers[5] += 1
        # 9, 10
        if registers[5] > registers[4]:
            # 12
            registers[3] += 1
            # 13, 14
            if registers[3] > registers[4]:
                # 16
                print(registers[0])
                return
            # 2
            registers[5] = 1


def method4(registers, ip_reg, instructions):
    for i in range(1, registers[4]+1):
        for j in range(1, registers[4]+1):
            # if i * j == total, add i
            if i*j == registers[4]:
                registers[0] += i
                break
    print(registers[0])


def method5(registers, ip_reg, instructions):
    result = registers[0]
    v = registers[4]
    for i in range(1, v+1):
        if v % i == 0:
            result += i
    print(result)


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
seti 0 4 1"""

ip_reg = 1

instructions = data.splitlines()

# line = 0
# for i in instructions:
#     opcode, a, b, c = i.split()
#     explain(line, opcode, a, b, c)
#     line += 1


# lines 17 to 35 means :
# #4 = 2*2*19*11 + 6*22+2
# 836 + 134 = 970
# #2 = ((27 * 28 + 29) * 30 * 14) * 32
#
# #4 = #4 + #2
#
# #2 = 10550400
# #4 = 10551370

# lines 0 to 16 :
"""
1 #3 = 1
2 #5 = 1
3 #2 = #3*#5 = 1
4 #2 = 1 if #2 == #4 else 0
5 jump to 7 if #2 == 1
6 jump to 8 if #2 == 0
7 #0 += #3
8 #5 += 1
9 #2 = 1 if #5 > #4 else 0
10 jump to 12 if #2 == 1
11 jump to 3
12 #3 += 1
13 #2 = 1 if #3 > #4
14 jump to 16 if #2 == 1
15 jump to 2
16 jump to 256 (halt)


eq.

#2 = 10550400
#4 = 10551370
#3 = 1

while #3 <= #4:
  #5 = 1
  while #5 <= #4:
    #2 = #3 * #5
    if #3 * #5 != #4:
        #0 += #3
    #5 += 1
  #3 += 1

so :

for #3 in range(1, 10551370 + 1):
    for #5 in range (1, 10551370 + 1):
        #2 = #3 * #5
        if #3 * #5 == #4
            #0 += #3
        
so with #3 = 1 and #5 = 10551370, #3 * #5 == #4

so :

a = 1
for i in range(1, 10551370+1):
    if 10551370 is divisible by i, add i to a
print(a)

"""

registers = [0, 0, 0, 0, 10551370, 0]

ip_reg = 1

instructions = data.splitlines()
# method1(deepcopy(registers), ip_reg, instructions)
# method2(deepcopy(registers), ip_reg, instructions)
# method3(deepcopy(registers), ip_reg, instructions)
# method4(deepcopy(registers), ip_reg, instructions)
method5(deepcopy(registers), ip_reg, instructions)
#
# a = 1
# for i in range(1, registers[4]):
#     a += i
# print(a)
