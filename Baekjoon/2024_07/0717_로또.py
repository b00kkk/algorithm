#BOJ 6603
import sys

def dfs():
    if len(lotto)==7:
        for i in lotto:
            if i!=0:
                print(i,end=' ')
        return print()
    for i in range(k):
        if lotto[-1]<s[i]:
            lotto.append(s[i])
            dfs()
            lotto.pop()

while True:
    num=list(map(int,sys.stdin.readline().split()))
    lotto=[0]
    if num[0]==0:
        break
    if len(num)>1:
        k,s=num[0],num[1:]
        s.sort()
        dfs()
    print()