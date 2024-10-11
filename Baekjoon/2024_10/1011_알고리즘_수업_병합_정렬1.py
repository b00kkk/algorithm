#BOJ 24060
import sys
input=sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))
result=[]
def merge_sort(A):
    if len(A)==1:
        return A
    q=(len(A)+1)//2
    L=merge_sort(A[:q])
    R=merge_sort(A[q:])
    i=0
    j=0
    tmp=[]
    while i<len(L) and j<len(R):
        if L[i] < R[j]:
            tmp.append(L[i])
            result.append(L[i])
            i += 1
        else:
            tmp.append(R[j])
            result.append(R[j])
            j += 1

    while i <len(L):
        tmp.append(L[i])
        result.append(L[i])
        i += 1
    while j <len(R):
        tmp.append(R[j])
        result.append(R[j])
        j+=1
    return tmp

merge_sort(A)

if len(result)>=K:
    print(result[K-1])
else:
     print(-1)