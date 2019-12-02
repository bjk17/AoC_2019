#!/usr/bin/env python

lines = open("input.txt").read().split()

total_fuel = 0
for line in lines:
    total_fuel += int(float(line) / 3) - 2

print(total_fuel)
