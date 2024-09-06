#BOJ 2343
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
guitar=list(map(int,input().split()))

start=max(guitar)
end=sum(guitar)
answer=0

while start<=end:
    mid=(start+end)//2
    count=1
    g_sum=0

    for g in guitar:
        if g_sum+g<=mid:
            g_sum+=g
        else:
            count+=1
            g_sum=g

    if count>M:
        start=mid+1
    else:
        answer=mid
        end=mid-1
print(answer)