#!/usr/bin/env python3

def readint():
    return int(input())

def readints():
    return map(int, input().split())

def readline():
    return str(input())

T = readint()
for case in range(T):
    last = '+'
    result = 0
    data = list(readline())
    data.reverse()
    for car in data:
        if last != car:
            result += 1
            last = car
    print("Case #%d: %s" % (case+1, result))
