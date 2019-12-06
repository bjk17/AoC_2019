#!/usr/bin/env python


class ReverseOrbitMap:
    def __init__(self):
        self._romap = dict()

    def insert_orbit(self, parent, child):
        self._romap[child] = parent

    def get_path(self, from_object, to_object):
        path = list()
        pointer = from_object
        while pointer != to_object:
            parent = self._romap[pointer]
            path.append(parent)
            pointer = parent

        return list(reversed(path))


reverse_orbit_map = ReverseOrbitMap()
for line in open("input.txt").read().split():
    parent, child = line.split(")")
    reverse_orbit_map.insert_orbit(parent, child)

path_to_YOU = reverse_orbit_map.get_path("YOU", "COM")
path_to_SAN = reverse_orbit_map.get_path("SAN", "COM")

i = 0
while path_to_YOU[i] == path_to_SAN[i]:
    i += 1

print(len(path_to_YOU) + len(path_to_SAN) - 2 * i)
