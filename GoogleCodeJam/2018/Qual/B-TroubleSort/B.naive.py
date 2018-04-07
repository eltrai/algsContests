#!/usr/bin/env python3

def readint():
    return int(input())
def readints():
    return map(int, input().split())
def readline():
    return str(input())

def TroubleSort(L):
    done = False
    while not done:
        done = True
        for i in range(len(L)-2):
            if L[i] > L[i+2]:
                done = False
                t = L[i]
                L[i] = L[i+2]
                L[i+2] = t

T = readint()
for case in range(T):
    l = readint()
    ss = list(readints())
    TroubleSort(ss)
    result = "OK"
    for i in range(len(ss)-1):
        if ss[i] > ss[i+1]:
            result = i
            break
    print("Case #%d: %s" % (case+1, result))
