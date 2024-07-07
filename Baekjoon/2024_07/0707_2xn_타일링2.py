#BOJ 11727
import sys
n=int(sys.stdin.readline())
tile=[1,3]
for i in range(2,n):
    if i%2==0:
        tile.append(tile[i-1]*2-1)
    else:
        tile.append(tile[i-1]*2+1)
print(tile[n-1]%10007)