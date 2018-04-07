#!/usr/bin/env python3

def readint():
    return int(input())
def readints():
    return map(int, input().split())
def readline():
    return str(input())

def damage(sequence):
    d = 1
    td = 0
    for l in sequence:
        if l == 'S':
            td += d
        else:
            d*=2
    return td

T = readint()
for case in range(T):
    inp = input().split(" ")
    shield = int(inp[0])
    sequence = inp[1]
    mod = 0
    result = "IMPOSSIBLE"
    while True:
        curDam = damage(sequence)
        if (curDam <= shield):
            result = str(mod)
            break
        oldsequence = sequence
        sequence = sequence[::-1].replace("SC", "CS", 1)[::-1]
        if (oldsequence == sequence):
            break
        mod += 1
    print("Case #%d: %s" % (case+1, result))
