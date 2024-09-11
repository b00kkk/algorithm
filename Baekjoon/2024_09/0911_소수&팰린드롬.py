#BOJ 1747
import sys
input=sys.stdin.readline

N=int(input())

def is_prime(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5+1)):
        if x%i==0:
            return False
    return True

while True:
    s=str(N)
    c=0
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]:
            c+=1
            continue
    if c>0:
        N+=1
        continue
 
    if is_prime(N):
        print(N)
        break
    else:
        N+=1