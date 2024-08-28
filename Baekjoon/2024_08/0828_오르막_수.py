#BOJ 11057
import sys
import math
input=sys.stdin.readline

N=int(input())
result=math.comb(N+10-1,N)
#중복 조합 공식 이용
#n+r-1, r
#n=10, r=N을 대입
print(result%10007)