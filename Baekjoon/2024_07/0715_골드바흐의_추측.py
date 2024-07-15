#BOJ 9020
import sys
t=int(sys.stdin.readline())

dic={}
def prime(k):
    for i in range(2,k):
        if k%i==0:
            return prime(k-1)
    if k not in dic:
        dic[k]=k
    return dic[k]

for i in range(t):
    n=int(sys.stdin.readline())
    a=n//2
    b=n
    while a+b!=n:
        a=prime(a)
        b=n-a
        if b==prime(b):
            break
        a-=1
    print(a,b)