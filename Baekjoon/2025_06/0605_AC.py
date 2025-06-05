# BOJ 5430
import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    p=input().strip()
    n=int(input())
    arr=input().strip()
    x=arr[1:-1]
    if x:
        x=deque(map(int,x.split(",")))
    else:
        x=deque()

    error=False
    reverse_flag=False

    for i in p:
        if i=="R":
            reverse_flag=not reverse_flag
        elif i=="D":
            if not x:
                print("error")
                error=True
                break
            else:
                if reverse_flag:
                    x.pop()
                else:
                    x.popleft()

    if error:
        continue
    if reverse_flag:
        x.reverse()
    print("[" + ",".join(map(str, x)) + "]")