#BOJ 2777
import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    num=[]
    if N==1:
        print(1)
        continue
    for i in range(9,1,-1):
        while N%i==0:
            num.append(i)
            N//=i
    if N > 1:
        print(-1)
    else:
        num.sort()
        result = ''.join(map(str, num))
        print(len(result))