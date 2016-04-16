#!/usr/bin/env python3

def readint():
    return int(input())

def readints():
    return map(int, input().split())

def readline():
    return str(input())

T = readint()
for case in range(T):
    K,C,S = readints()
    if C*S<K:
        result = "IMPOSSIBLE"
    else:
        res = []
        s = 0
        k = 0
        while k<K:
            new = 0
            for i in range(1, C+1):
                toadd = k*(K**(C-i))
                if k >= K:
                    new += K**(C-i+1)-1
                    break
                else:
                    new += toadd
                    k += 1
            res.append(new+1)
            s += 1
        result = ' '.join(map(str, res))





    print("Case #%d: %s" % (case+1, result))
