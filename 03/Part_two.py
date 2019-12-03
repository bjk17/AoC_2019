#!/usr/bin/env python


def wpath_to_vldict(wpath):
    # wire path to "visited positions"/length key/value dictionary
    vldict = dict()
    pos = [0, 0]
    distance = 0
    for steps in wpath.split(","):
        direction, length = steps[0], int(steps[1:])
        for step in range(1, length + 1):
            distance += 1
            if direction == 'U':
                pos[1] += 1
            elif direction == 'D':
                pos[1] -= 1
            elif direction == 'R':
                pos[0] += 1
            elif direction == 'L':
                pos[0] -= 1

            tpos = tuple(pos)
            if tpos not in vldict:
                vldict[tpos] = distance 

    return vldict


wpath1, wpath2 = list(open("input.txt").read().split())
vldict1, vldict2 = wpath_to_vldict(wpath1), wpath_to_vldict(wpath2)

intersections = vldict1.keys() & vldict2.keys()
print(min(vldict1[pos] + vldict2[pos] for pos in intersections))
