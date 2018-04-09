#!/usr/bin/python

from math import sqrt,floor

def readint ():
	return int(input())
def readarray ( f ):
	return map(f, input().split())

def solve(r,t):
    i=0
    while t>0:
        t -= 2*r+1
        r += 2
        i += 1
    if t==0:
        return i
    else:
        return i-1

cases = readint()
for k in range(cases):
	r, t = readarray(int)
	print('Case #' + str(k+1) + ': ' + str(solve(r, t)))
