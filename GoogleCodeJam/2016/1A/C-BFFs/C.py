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
    bffs = list(readints())
    result = 0
    resultFromLines = 0
    lines = defaultdict(lambda :defaultdict(lambda :(0, [])))
    for first in range(N):
        current = first
        last = -1
        streak = [] 
        while(current not in streak):
            streak.append(current)
            lastlast = last
            last = current
            current = bffs[current]-1
        else:
            if current == lastlast:
                index = [current,last]
                index.sort()
                index2 = streak[-2]
                index = tuple(index)
                if len(streak) > lines[index][index2][0]:
                    lines[index][index2] = (len(streak), streak)
                result = max(result, len(streak))
                log.info("Line found : %d, %s (%s, %s)" % (len(streak), repr(streak), index, index2))
            elif current == first:
                result = max(result, len(streak))
                log.info("Cicle found : %s " % (repr(streak)))
            else:
                continue
    log.debug("Without lines : %d" % (result))
    log.debug(lines)
    for l,lv in lines.items():
        thisline = lv[l[0]][0] + lv[l[1]][0] - 2
        log.info("LINE SUM : %s (%s) + %s (%s)" % (lv[l[0]][1], lv[l[0]][0], lv[l[1]][1], lv[l[1]][0]))
        resultFromLines += thisline


    result = max(result, resultFromLines)







    print("Case #%d: %s" % (case+1, result))
