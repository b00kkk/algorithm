# BOJ 1874
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
target=[int(input()) for i in range(n)]
stack=deque()
result=[]
result_n=[]
now=1

for i in range(n):
    while now<=target[i]:
        stack.append(now)
        now+=1
        result.append('+')
    result.append('-')
    result_n.append(stack.pop())

if result_n!=target:
    print('NO')
else:
    print(*result,sep='\n')