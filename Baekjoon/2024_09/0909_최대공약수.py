#BOJ 1850
import sys
import math
input=sys.stdin.readline

A,B=map(int,input().split())
gcd=math.gcd(A,B)
print('1'*gcd)

#math.gcd 라이브러리 사용
#최대공약수를 구해주는 라이브러리