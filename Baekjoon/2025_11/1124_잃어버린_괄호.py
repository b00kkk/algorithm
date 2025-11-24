# BOJ 1541
import sys
input=sys.stdin.readline

s=input().strip()
part=s.split('-')
s_sum=sum(map(int,part[0].split('+')))
for i in part[1:]:
    s_sum-=sum(map(int,i.split('+')))
print(s_sum)