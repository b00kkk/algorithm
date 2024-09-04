#BOJ 6588
import sys
input=sys.stdin.readline

check=[1]*1000001
for i in range(2,1001):
    if check[i]:
        for j in range(2*i,1000001,i):
            check[j]=0

while True:
    n=int(input())
    if n==0:
        break
    k=0
    for i in range(3,len(check),2):
        if check[i] and check[n-i]:
            k+=1
            break
    if k!=0:
        print(n,'=',i,'+',n-i)
    else:
        print("Goldbach's conjecture is wrong.")