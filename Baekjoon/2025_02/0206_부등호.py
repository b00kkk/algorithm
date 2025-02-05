# BOJ 2529
import sys
import itertools
input=sys.stdin.readline

k=int(input())
A=list(input().strip().split())
num=[i for i in range(10)]
numlist=itertools.permutations(num,k+1)
answer=[]

for n in list(numlist):
    flag=True
    for i in range(k):
        if A[i]=='<' and not n[i]<n[i+1]:
            flag=False
            break
        if A[i]=='>' and not n[i]>n[i+1]:
            flag=False
            break
    int_str=''
    if flag:
        for j in n:
            int_str+=str(j)
        answer.append(int(int_str))

answer_max=max(answer)
answer_min=min(answer)

if len(str(answer_max)) != k+1:
    answer_max = '0'+str(answer_max)
if len(str(answer_min)) != k+1:
    answer_min='0'+str(answer_min)

print(answer_max)
print(answer_min)