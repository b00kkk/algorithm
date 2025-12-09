# BOJ 10971

import sys
input=sys.stdin.readline
n=int(input())
w=[]
answer=sys.maxsize
for i in range(n):
    w.append(list(map(int,input().split())))

def dfs(start,next,value):
    global answer
    if len(visited)==n:
        if w[next][start]!=0:
            answer=min(value+w[next][start],answer)
        return
    for i in range(n):
        if w[next][i]!=0 and i not in visited and value<answer:
            visited.append(i)
            dfs(start,i,value+w[next][i])
            visited.pop()
for i in range(n):
    visited=[i]
    dfs(i,i,0)
print(answer)