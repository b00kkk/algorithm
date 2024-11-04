#BOJ 24416
import sys
input=sys.stdin.readline

n=int(input())

def fibonacci(n):
    c=0
    f=[0]*(n+1)
    f[1]=1
    f[2]=1
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
        c+=1
    return print(f[n],c)

fibonacci(n)