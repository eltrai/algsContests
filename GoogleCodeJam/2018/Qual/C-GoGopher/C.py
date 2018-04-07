#!/usr/bin/env python3
import sys

def readint():
    return int(input())
def readints():
    return map(int, input().split())
def readline():
    return str(input())

def newMatrix():
    return [[0 for x in range(3)] for y in range(3)]

def matrixFull(m):
    for i in range(3):
        for j in range(3):
            if m[i][j] == 0:
                return False
    return True

def run():
    A = readint()
    square = newMatrix()
    offset=0
    print("2 2")
    while True:
        I, J = readints()
        if I == -1:
            sys.exit()
        elif I == 0:
            return
        else:
            square[I-offset-1][J-1] = 1
            if matrixFull(square):
                offset += 3
                square = newMatrix()
            print("%d %d" % (2+offset, 2))

T = readint()
for case in range(T):
    run()

