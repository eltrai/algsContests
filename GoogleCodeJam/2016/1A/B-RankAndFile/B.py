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

#Go Go Go
T = readint()
for case in range(T):
    N = readint()
    vals = defaultdict(lambda :0)
    for j in range(2*N-1):
        line = readints()
        for v in line:
            vals[v] += 1
    log.debug(vals)
    sol = []
    for v,i in vals.items():
        if i%2 != 0:
            sol.append(v)
    sol.sort()
    result = ' '.join(map(str, sol))





    print("Case #%d: %s" % (case+1, result))
