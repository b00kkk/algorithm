#BOJ 17253
import sys
input=sys.stdin.readline

N=int(input())

k=0
while True:
    if 3**k > N:
        break
    else:
        k+=1

j=1
for i in range(k,-1,-1):
    if N-3**i<0:
        pass
    elif N-3**i==0:
         j=0
    else:
        N-=3**i

if j==0:
    print('YES')
else:
    print('NO')