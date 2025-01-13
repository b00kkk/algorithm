#BOJ 2776
import sys
input=sys.stdin.readline

def binary(a,b,i):
    while a<=b:
        c=(a+b)//2
        if i==note1[c]:
            return 1
        elif i>note1[c]:
            a=c+1
        else:
            b=c-1
    return 0          

T=int(input())
for _ in range(T):
    N=int(input())
    note1=list(map(int,input().split()))
    M=int(input())
    note2=list(map(int,input().split()))
    note1.sort()
    for i in note2:
        a,b=0,N-1
        print(binary(a,b,i))