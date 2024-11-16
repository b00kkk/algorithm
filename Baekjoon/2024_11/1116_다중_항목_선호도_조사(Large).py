#BOJ 25327
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = defaultdict(int)
for _ in range(n):
    tmp = ' '.join(list(map(str, input().rstrip().split())))
    dic[tmp] += 1

for _ in range(m):
    sub, fru, color = map(str, input().rstrip().split())
    cnt = 0
    
    for i in dic:
        s, f, c = i.split()
        
        if (sub == '-' or sub == s) and (fru == '-' or fru == f) and (color == '-' or color == c):
            cnt += dic[i]
            
    print(cnt)