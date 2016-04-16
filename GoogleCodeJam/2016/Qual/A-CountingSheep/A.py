#!/usr/bin/env python3

def readint():
    return int(input())

def readints():
    return map(int, input().split())

def readline():
    return str(input())

T = readint()
for case in range(T):
    N = readint()
    if N == 0:
        result = "INSOMNIA"
    else:
        k = 0
        s = set()
        while len(s) < 10:
            s.update(list(str((k+1)*N)))
            k += 1
        result = str(k*N)





    print("Case #%d: %s" % (case+1, result))
