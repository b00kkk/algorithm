#BOJ 1406
import sys
s=sys.stdin.readline().strip()
m=int(sys.stdin.readline())
n=len(s)
left=list(s)
right=[]
for i in range(m):
    order=sys.stdin.readline().strip()
    if order=='L':
        if left:
            right.append(left.pop())
    elif order=='D':
        if right:
            left.append(right.pop())
    elif order=='B':
        if left:
            left.pop()
    elif 'P' in order:
        p,a=order.split()
        left.append(a)
print(''.join(left)+''.join(reversed(right)))