#BOJ 4134
import sys
input = sys.stdin.readline

t=int(input())

def is_prime(n):
    if n==0:
        return 2
    if n==1:
        return 2
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return is_prime(n+1)
    return n

for _ in range(t):
    n=int(input())
    print(is_prime(n))