# BOJ 9019
# PyPy3 통과

import sys
from collections import deque
input=sys.stdin.readline

def D(n):
    return 2*n % 10000

def S(n):
    if n==0:
        return 9999
    return n-1

def L(n):
    return n // 1000 + (n % 1000) * 10

def R(n):
    return (n % 10) * 1000 + n // 10

T=int(input())
for _ in range(T):
    A,B=map(int,input().split())
    visited=[0]*10000
    queue=deque()
    queue.append((A,""))
    visited[A]=1

    while queue:
        cur,ops=queue.popleft()

        if cur==B:
            print(ops)
            break

        for cmd, next_num in [('D',D(cur)),('S',S(cur)),('L',L(cur)),('R',R(cur))]:
            if not visited[next_num]:
                queue.append((next_num, ops+cmd))
                visited[next_num]=1

