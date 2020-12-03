#!/usr/bin/env python3

import re
import numpy as np

def indatakrossen(fn):
    with open("data/{:s}".format(fn), "r") as filbunke:
        return [l.rstrip() for l in filbunke.readlines()]

def everscream():
    representationskontot = [int(n) for n in indatakrossen("1a.txt")]
    print([(2020-a)*a for a in representationskontot if 2020-a in representationskontot])
    # Lol brute force orka krångla
    print([a*d*e for a in representationskontot for d in representationskontot[::-1] for e in representationskontot if a+d+e == 2020][0])

def haigography_of_saint_nicholaus():
    rules, passwords = zip(*[s.split(': ') for s in indatakrossen("2.txt")])

    def hard_presents(r):
        return r.replace("-", " ").split(" ")

    bag_o_presents = list(zip(map(hard_presents, rules), passwords))
    print(sum(1 for p, q in bag_o_presents if int(p[0]) <= q.count(p[2]) <= int(p[1])))
    print(sum(1 for p, q in bag_o_presents if (p[2] in q[int(p[0])-1]) ^ (p[2] in q[int(p[1])-1])))

def de_anima():
    skidbacke = np.array([list(w) for w in indatakrossen("3.txt")])
    tall, tjocc = skidbacke.shape
    def kraschtest(xskip, yskip):
        x = y = trees = 0
        while y < tall:
            trees += '#' in skidbacke[y, x % tjocc]
            x += xskip
            y += yskip
        return(trees)
    backar = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(np.product([kraschtest(*backe) for backe in backar]))


if __name__ == "__main__":
    problems = {
        1: everscream,
        2: haigography_of_saint_nicholaus,
        3: de_anima,
    }

    problems[3]()
