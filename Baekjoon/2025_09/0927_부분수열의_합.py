# BOJ 1182
import sys
n,s=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
c=0

def add(idx,a):
    global c
    if idx>=n:
        return
    a+=num[idx]
    if a==s:
        c+=1
    add(idx+1,a)
    add(idx+1,a-num[idx])
add(0,0)
print(c)