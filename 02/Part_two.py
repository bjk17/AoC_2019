#!/usr/bin/env python
import itertools

intcodes_original = list(map(int, open("input.txt").read().split(",")))
for noun, verb in itertools.product(range(100), repeat=2):
    
    intcodes = intcodes_original.copy()
    intcodes[1] = noun
    intcodes[2] = verb

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

    if intcodes[0] == 19690720:
        print(100 * noun + verb)
        break
