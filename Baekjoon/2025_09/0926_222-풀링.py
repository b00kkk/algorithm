# BOJ 17829
import sys
input=sys.stdin.readline

N=int(input())

nn=[]
for _ in range(N):
    arr=list(map(int,input().split()))
    nn.append(arr)

while N!=1:
    new_arr=list([0]*(N//2) for _ in range(N//2))
    for i in range(0,N,2):
        for j in range(0,N,2):
            next_nn=[nn[i][j], nn[i][j+1], nn[i+1][j], nn[i+1][j+1]]
            next_nn.sort()
            new_arr[i//2][j//2]=next_nn[2]
    nn=new_arr
    N=N//2

print(new_arr[0][0])
