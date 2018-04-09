#!/usr/bin/env python3
# *-* coding: utf-8 *-*

#Let's set up logging
import logging
logging.basicConfig(level=logging.WARNING)
#logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

#Useful libs
from collections import defaultdict

#Useful functions
def readint():
    return int(input())

def readints():
    return map(int, input().split())

def readline():
    return str(input())

def isValid(num_i, orig):
    if num_i < 0:
        return False
    num = list(str(num_i))
    while len(num)<len(orig):
        num.insert(0, '0')
    if len(num) != len(orig):
        return False
    for i in range(len(orig)):
        if orig[i] == '?':
            pass
        elif orig[i] == num[i]:
            pass
        else:
            return False
    return True

def maxSeq(num):
    for i in range(len(num)):
        if num[i] == '?':
            num[i] = '9'
    return num

def minSeq(num):
    for i in range(len(num)):
        if num[i] == '?':
            num[i] = '0'
    return num

def generate(prefix, suffix, f):
    return int(str(prefix) + ''.join(f(suffix[:])))


#Go Go Go
T = readint()
for case in range(T):
    C,J = map(list, readline().split())
    Corig = C[:]
    Jorig = J[:]
    #compatible:
    for i in range(len(C)):
        if C[i] == '?':
            if J[i] == '?':
                C[i] = '0'
                J[i] = '0'
            else:
                C[i] = J[i]
        elif J[i] == '?':
            J[i] = C[i]
        elif C[i] == J[i]:
            pass
        else:
            Cprefix = 0
            Jprefix = 0
            if i>0:
                Cprefix = int(''.join(C[:i]))
                Jprefix = int(''.join(J[:i]))
            if C[i] > J[i]:
                Cn = generate(Cprefix, C[i:], minSeq)
                Jn = generate(Jprefix, J[i:], maxSeq)
            else:
                Cn = generate(Cprefix, C[i:], maxSeq)
                Jn = generate(Jprefix, J[i:], minSeq)
            #attempt minus C
            C2 = generate(Cprefix-1, C[i:], maxSeq)
            J2 = generate(Jprefix, J[i:], minSeq)
            if isValid(C2, Corig) and isValid(J2, Jorig) and abs(C2-J2) <= abs(Cn-Jn):
                Cn = C2
                Jn = J2
            #attempt minus J
            C2 = generate(Cprefix, C[i:], minSeq)
            J2 = generate(Jprefix-1, J[i:], maxSeq)
            if isValid(C2, Corig) and isValid(J2, Jorig) and abs(C2-J2) <= abs(Cn-Jn):
                Cn = C2
                Jn = J2
            #attempt max C
            C2 = generate(Cprefix+1, C[i:], minSeq)
            J2 = generate(Jprefix, J[i:], maxSeq)
            if isValid(C2, Corig) and isValid(J2, Jorig) and abs(C2-J2) < abs(Cn-Jn):
                Cn = C2
                Jn = J2
            #attempt max J
            C2 = generate(Cprefix, C[i:], maxSeq)
            J2 = generate(Jprefix+1, J[i:], minSeq)
            if isValid(C2, Corig) and isValid(J2, Jorig) and abs(C2-J2) < abs(Cn-Jn):
                Cn = C2
                Jn = J2
            if C[i] > J[i]:
                C2 = generate(Cprefix-1, C[i:], minSeq)
                J2 = generate(Jprefix-1, J[i:], maxSeq)
            else:
                C2 = generate(Cprefix-1, C[i:], maxSeq)
                J2 = generate(Jprefix-1, J[i:], minSeq)
            if isValid(C2, Corig) and isValid(J2, Jorig) and abs(C2-J2) <= abs(Cn-Jn):
                Cn = C2
                Jn = J2

            J = list(str(Jn))
            C = list(str(Cn))
            while len(J)<len(Jorig):
                J.insert(0, '0')
            while len(C)<len(Corig):
                C.insert(0, '0')
            break


            

    result = ''.join(C) + ' ' + ''.join(J)










    print("Case #%d: %s" % (case+1, result))
