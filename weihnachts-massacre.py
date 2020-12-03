#!/usr/bin/env python3

def indatakrossen(fn):
  with open("data/{:s}".format(fn), "r") as file:
    return [l for l in file.readlines()]

def everscream():
  representationskontot = [int(n) for n in indatakrossen("1a.txt")]
  print([(2020-a)*a for a in representationskontot if 2020-a in representationskontot])
  # Lol brute force orka krångla
  print([a*d*e for a in representationskontot for d in representationskontot[::-1] for e in representationskontot if a+d+e == 2020][0])


if __name__ == "__main__":
  problems = {
    1: everscream,
  }

  problems[1]()
