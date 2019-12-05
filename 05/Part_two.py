#!/usr/bin/env python
import itertools


def decode_intcode(intcode):
    A  = intcode // 10000 % 10
    B  = intcode // 1000 % 10
    C  = intcode // 100 % 10
    DE = intcode % 100

    return A, B, C, DE


intcodes = list(map(int, open("input.txt").read().split(",")))

i = 0
while i < len(intcodes):
    intcode = intcodes[i]
    A, B, C, opcode = decode_intcode(intcode)

    if opcode == 99:
        break

    val1 = intcodes[intcodes[i + 1]] if C == 0 else intcodes[i + 1]
    if opcode in (1, 2, 5, 6, 7, 8):
        val2 = intcodes[intcodes[i + 2]] if B == 0 else intcodes[i + 2]

    write_location = intcodes[i + 3] if A == 0 else i + 3

    if opcode == 1:
        intcodes[write_location] = val1 + val2
        i += 4
    elif opcode == 2:
        intcodes[write_location] = val1 * val2
        i += 4
    elif opcode == 3:
        intcodes[write_location] = 5
        i += 2
    elif opcode == 4:
        if val1 != 0:
            print(val1, end='', flush=True)
        i += 2
    elif opcode == 5:
        if val1 != 0:
            i = val2
        else:
            i += 3
    elif opcode == 6:
        if val1 == 0:
            i = val2
        else:
            i += 3
    elif opcode == 7:
        intcodes[write_location] = 1 if val1 < val2 else 0
        i += 4
    elif opcode == 8:
        intcodes[write_location] = 1 if val1 == val2 else 0
        i += 4
    else:
        raise ValueError(f"Unknown opcode {opcode}")

print()
