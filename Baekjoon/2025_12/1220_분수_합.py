# BOJ 1735
import sys
import math
input=sys.stdin.readline

a,b=map(int,input().split())
c,d=map(int,input().split())
ja=a*d+c*b
mo=b*d
i=math.gcd(ja,mo)
ja//=i
mo//=i
print(ja,mo)