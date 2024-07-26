#BOJ 14889
import sys
from itertools import combinations
input = sys.stdin.readline
n=int(input())
s=[]

for i in range(n):
    s.append(list(map(int,input().split())))

result=sys.maxsize

for i in list(combinations(range(n),n//2)):
    start=0
    rink=0
    r_list=list(range(n))
    for j in i:
        r_list.remove(j)
    for a,b in list(combinations(i,2)):
        start+=s[a][b]+s[b][a]
    for a,b in combinations(r_list,2):
        rink+=s[a][b]+s[b][a]
    result=min(result,abs(start-rink))
print(result)