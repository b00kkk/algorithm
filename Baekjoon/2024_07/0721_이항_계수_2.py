#BOJ 11051
import sys
from math import factorial
n,k=map(int,sys.stdin.readline().split())
c=(factorial(n)//factorial(k)//factorial(n-k))%10007
print(c)