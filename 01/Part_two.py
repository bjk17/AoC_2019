#!/usr/bin/env python

lines = open("input.txt").read().split()

total_fuel = 0
for line in lines:
    fuel = int(float(line) / 3) - 2
    while fuel > 0:
        total_fuel += fuel
        fuel = int(fuel / 3) - 2

print(total_fuel)
