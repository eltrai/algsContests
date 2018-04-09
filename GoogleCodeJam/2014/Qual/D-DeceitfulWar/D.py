#!/usr/bin/python

def readint ():
	return int(input())
def readarray ( f ):
	return map(f, input().split())

def solveWar(N, Bn, Bk):
	score = 0
	while len(Bn) > 0:
		if Bn[-1] > Bk[-1]:
			score += 1
			del Bk[0]
		else:
			del Bk[next(i for i in range(len(Bk)) if Bk[i] > Bn[-1])]
		del Bn[-1]
	return score

def solveDWar(N, Bn, Bk):
	score = 0
	while len(Bn) > 0:
		#print("N:", Bn)
		#print("K:", Bk)
		if Bn[0] < Bk[0]:
			del Bn[0]
			del Bk[-1]
		else:
			score += 1
			del Bn[0]
			del Bk[0]
	return score

cases = readint()
for k in range(cases):
	N = readint()
	Bn = sorted(readarray(float))
	Bk = sorted(readarray(float))
	print('Case #' + str(k+1) + ': ' + str(solveDWar(N, Bn.copy(), Bk.copy())) + ' ' + str(solveWar(N, Bn, Bk)))
