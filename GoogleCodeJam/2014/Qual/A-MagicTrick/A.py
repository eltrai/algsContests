#!/usr/bin/python

def readint ():
	return int(input())
def readarray ( f ):
	return map(f, input().split())

def solve(A, B):
	sol = list(set(A) & set(B))
	if len(sol) == 1:
		return sol[0]
	if len(sol) > 1:
		return "Bad magician!"
	return "Volunteer cheated!"

cases = readint()
for k in range(cases):
	num = readint()-1
	l = []
	for i in range(4):
		l.append(list(readarray(int)))
	num2 = readint() + 3
	for i in range(4):
		l.append(list(readarray(int)))
	print('Case #' + str(k+1) + ': ' + str(solve(l[num], l[num2])))
