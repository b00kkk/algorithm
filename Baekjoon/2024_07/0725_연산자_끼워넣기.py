#BOJ 14888
import sys
from itertools import permutations
input = sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
op=list(map(int,input().split()))
oper=[]
for i in range(4):
    if i==0:
        oper+=['+']*op[i]
    elif i==1:
        oper+=['-']*op[i]
    elif i==2:
        oper+=['*']*op[i]
    elif i==3:
        oper+=['/']*op[i]
chk=[]
for per in list(set(permutations(oper))):
    v=a[0]
    for i in range(len(per)):
        if per[i]=='+':
            v+=a[i+1]
        elif per[i]=='-':
            v-=a[i+1]
        elif per[i]=='*':
            v*=a[i+1]
        elif per[i]=='/':
            if v<0:
                v=abs(v)//a[i+1]
                v*=-1
            else:
                v//=a[i+1]
    chk.append(v)
print(max(chk))
print(min(chk))