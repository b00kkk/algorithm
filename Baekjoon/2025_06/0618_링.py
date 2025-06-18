# BOJ 3036
import sys
from fractions import Fraction
input = sys.stdin.readline

N=int(input())
r=list(map(int,input().split()))

r1=r[0]

for i in range(1,N):
    f= Fraction(r[i],r1)
    print(f"{f.denominator}/{f.numerator}")