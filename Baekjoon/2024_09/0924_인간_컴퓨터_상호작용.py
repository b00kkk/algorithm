#BOJ 16139
import sys
input = sys.stdin.readline

S=input().strip()
array=[[0]*26 for _ in range(len(S)+1)]

for i in range(len(S)):
    c=ord(S[i])-97
    array[i+1]=array[i][:]
    array[i+1][c]+=1

q=int(input())
for _ in range(q):
    a,l,r=map(str,input().strip().split())
    a=ord(a)-97
    l=int(l)
    r=int(r)
    print(array[r+1][a]-array[l][a])