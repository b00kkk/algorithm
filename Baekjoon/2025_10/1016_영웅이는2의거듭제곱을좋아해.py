# BOJ 20153
import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int,input().split()))

def bit_count(arr):
    max_bit=max(arr).bit_length()
    count=[0]*max_bit
    for x in arr:
        for k in range(max_bit):
            count[k] += (x>>k) & 1
    return count

result=bit_count(nums)
ans=0
for i ,cnt in enumerate(result):
    if cnt%2:
        ans+=(1<<i)

best = ans
for v in nums:
    cand=ans^v
    if cand > best:
        best=cand

print(f"{best}{best}")