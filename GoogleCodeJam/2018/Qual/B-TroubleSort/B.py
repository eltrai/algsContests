#!/usr/bin/env python3

def readint():
    return int(input())
def readints():
    return map(int, input().split())
def readline():
    return str(input())

T = readint()
for case in range(T):
    l = readint()
    sequence = list(readints())
    s1 = sorted(sequence[::2])
    s2 = sorted(sequence[1::2])
    result = "OK"
    for i in range(len(s2)):
        if s1[i] > s2[i]:
            result = i*2
            break
        elif i+1 < len(s1) and s2[i] > s1[i+1]:
            result = i*2+1
            break
    print("Case #%d: %s" % (case+1, result))
