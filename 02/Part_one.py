#!/usr/bin/env python

intcodes = list(map(int, open("input.txt").read().split(",")))

# Restoring the Gravity assist program to the "1202 program alarm" state
intcodes[1] = 12
intcodes[2] = 2

# Running the Intcode program
for i in range(0, len(intcodes), 4):
    code = intcodes[i]
    if code == 99:
        break

    val1 = intcodes[intcodes[i + 1]]
    val2 = intcodes[intcodes[i + 2]]
    if code == 1:
        intcodes[intcodes[i + 3]] = val1 + val2
    elif code == 2:
        intcodes[intcodes[i + 3]] = val1 * val2

print(intcodes[0])
