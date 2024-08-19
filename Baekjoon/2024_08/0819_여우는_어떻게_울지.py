#BOJ 9536
import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    fox=list(map(str,input().strip().split()))
    while True:
        s=input().strip()
        if s=='what does the fox say?':
            break
        while True:
            if s.split(' goes ')[1] in fox:
                fox.remove(s.split(' goes ')[1])
            else:
                break
    print(*fox)