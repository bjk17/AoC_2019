#!/usr/bin/env python
from collections import defaultdict


class OrbitMap:
    def __init__(self):
        self._omap = defaultdict(list)

    def insert_orbit(self, parent, child):
        self._omap[parent].append(child)

    def count_orbits(self, parent, depth=0):
        return depth + sum(
            self.count_orbits(child, depth+1) for child in self._omap[parent])


orbit_map = OrbitMap()
for line in open("input.txt").read().split():
    parent, child = line.split(")")
    orbit_map.insert_orbit(parent, child)

print(orbit_map.count_orbits("COM"))
