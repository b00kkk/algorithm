#BOJ 9663
import sys
input=sys.stdin.readline

N=int(input())
ans=0
row=[0]*N

def is_promisig(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def n_queens(x):
    global ans
    if x==N:
        ans+=1
        return
    else:
        for i in range(N):
            row[x]=i
            if is_promisig(x):
                n_queens(x+1)

n_queens(0)
print(ans)

#PyPy3로 성공(Python3는 시간초과)