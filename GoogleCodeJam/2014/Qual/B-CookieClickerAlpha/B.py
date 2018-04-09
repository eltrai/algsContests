#!/usr/bin/python

def readint ():
	return int(input())
def readarray ( f ):
	return map(f, input().split())

def solve(C, F, X):
	rate = 2
	tspent = 0
	while X/rate > C/rate + X/(rate + F):
		tspent += C/rate		
		rate += F
	return tspent + X/rate

cases = readint()
for k in range(cases):
	C, F, X = readarray(float)
	print('Case #' + str(k+1) + ': ' + str(solve(C, F, X)))
