#!/usr/bin/env python3

import re
import numpy as np
import datetime

def indatakrossen(fn):
    with open("data/{:s}".format(fn), "r") as filbunke:
        return [l.rstrip() for l in filbunke.readlines()]

def everscream():
    representationskontot = [int(n) for n in indatakrossen("1a.txt")]
    print([(2020-a)*a for a in representationskontot if 2020-a in representationskontot])
    # Lol brute force orka krångla
    print([a*d*e for a in representationskontot for d in representationskontot[::-1] for e in representationskontot if a+d+e == 2020][0])

def hagiography_of_saint_nicholaus():
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

def malfunctioning_reindeer_mech():
    with open("data/4.txt", "r") as filbunke:
        passports = ''.join([l for l in filbunke.readlines()]).split("\n\n")
    passports = [dict(fields.split(':') for fields in p.split()) for p in passports]
    fuck_cid = [{k: v for k, v in passport.items() if k != 'cid'} for passport in passports]
    n_valid_passports = sum(1 for test in fuck_cid if len(test.keys()) == 7)
    print(n_valid_passports)
    tests = {
        'byr': lambda n: 1920 <= int(n) <= 2002,
        'iyr': lambda n: 2010 <= int(n) <= 2020,
        'eyr': lambda n: 2020 <= int(n) <= 2030,
        'hgt': lambda n: (150 <= int(n[:n.find('cm')]) <= 193) if('cm' in n) else ((59 <= int(n[:n.find('in')]) <= 76) if('in' in n) else False),
        'hcl': lambda n: len(n) == 7 and re.search(r'#[0-9a-f]{6}', n) is not None,
        'ecl': lambda n: len(n) == 3 and n in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        'pid': lambda n: len(n) == 9 and re.search(r'[0-9]{9}', n) is not None
    }

    print(sum(sum(tests[k](v) for k, v in p.items()) == 7 for p in fuck_cid))


if __name__ == "__main__":
    problems = {
        1: everscream,
        2: hagiography_of_saint_nicholaus,
        3: de_anima,
        4: malfunctioning_reindeer_mech
    }

    problems[datetime.datetime.today().day]()
