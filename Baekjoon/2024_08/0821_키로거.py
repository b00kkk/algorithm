#BOJ 5397
import sys
from collections import deque
input=sys.stdin.readline

L=int(input())
for _ in range(L):
    left=deque()
    right=deque()
    s=input().strip()
    for i in s:
        if i=='-':
            if left:
                left.pop()
        elif i=='<':
            if left:
                right.append(left.pop())
        elif i=='>':
            if right:
                left.append(right.pop())
        else:
            left.append(i)
    left+=(reversed(right))
    print("".join(left))