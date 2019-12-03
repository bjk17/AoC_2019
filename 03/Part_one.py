#!/usr/bin/env python


def wpath_to_vset(wpath):
    # wire path to "visited positions" set
    vset = set()
    pos = [0, 0]
    for steps in wpath.split(","):
        direction, length = steps[0], int(steps[1:])
        if direction == 'U':
            vset.update([(pos[0], pos[1] + step) for step in range(1, length + 1)])
            pos[1] += length
        elif direction == 'D':
            vset.update([(pos[0], pos[1] - step) for step in range(1, length + 1)])
            pos[1] -= length
        elif direction == 'R':
            vset.update([(pos[0] + step, pos[1]) for step in range(1, length + 1)])
            pos[0] += length
        elif direction == 'L':
            vset.update([(pos[0] - step, pos[1]) for step in range(1, length + 1)])
            pos[0] -= length

    return vset


def manhattan_distance(pos):
    return abs(pos[0]) + abs(pos[1])


wpath1, wpath2 = list(open("input.txt").read().split())
vset1, vset2 = wpath_to_vset(wpath1), wpath_to_vset(wpath2)
print(min(manhattan_distance(pos) for pos in vset1 & vset2))
