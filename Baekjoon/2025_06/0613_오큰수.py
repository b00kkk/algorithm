# BOJ 17298
import sys
input = sys.stdin.readline

A=int(input())
arr=list(map(int,input().split()))
answer=[-1]*A
stack=[]

for i in range(A):
    while stack and arr[stack[-1]] < arr[i]:
        index=stack.pop()
        answer[index]=arr[i]
    stack.append(i)

print(*answer)
