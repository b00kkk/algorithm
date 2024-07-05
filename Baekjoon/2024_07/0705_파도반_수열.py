#BOJ 9461
import sys
t=int(sys.stdin.readline())
pn={1:1,2:1,3:1,4:2,5:2}

def p_n(n):
    if n in pn:
        return pn[n]
    pn[n]=p_n(n-1)+p_n(n-5)
    return pn[n]


for i in range(t):
    n=int(sys.stdin.readline())
    print(p_n(n))