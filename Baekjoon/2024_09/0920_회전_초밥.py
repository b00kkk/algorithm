#BOJ 2531
import sys
from collections import defaultdict
input=sys.stdin.readline

N,d,k,c=map(int,input().split())
sushi = [int(input()) for _ in range(N)]
sushi_count = defaultdict(int)

for i in range(k):
    sushi_count[sushi[i]] += 1

sushi_count[c] += 1

result = len(sushi_count)

for i in range(1, N):
    new_sushi = sushi[(i + k - 1) % N]
    sushi_count[new_sushi] += 1
    
    old_sushi = sushi[i - 1]
    sushi_count[old_sushi] -= 1
    if sushi_count[old_sushi] == 0:
        del sushi_count[old_sushi]
    
    result = max(result, len(sushi_count))
    
print(result)

#defaultdict 사용법 알아두기