#BOJ 10986
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))

S = [0] * N
for i in range(N):
    S[i] = S[i - 1] + A[i]
    
C = [0] * M
answer = 0
for i in range(N):
    r = S[i] % M
    if (r == 0):
        answer += 1
    C[r] += 1
    
for i in range(M):
    if (C[i] > 1):
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)