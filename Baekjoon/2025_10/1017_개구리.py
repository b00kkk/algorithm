# BOJ 23797
import sys
input=sys.stdin.readline

S=input().strip()

arr=[]
endK=[]
endP=[]

for ch in S:
    if ch=='K':
        if endP:
            idx=endP.pop()
            arr[idx]+='K'
            endK.append(idx)
        else:
            arr.append('K')
            endK.append(len(arr)-1)

    else:
        if endK:
            idx=endK.pop()
            arr[idx]+='P'
            endP.append(idx)
        else:
            arr.append('P')
            endP.append(len(arr)-1)

print(len(arr))