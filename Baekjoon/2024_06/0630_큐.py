#BOJ 10845
import sys
n=int(sys.stdin.readline())
q=[]
for i in range(n):
    s=sys.stdin.readline().rstrip()
    if 'push' in s:
        p,q_int=s.split()
        q_int=int(q_int)
        q.append(q_int)
    elif s=='front':
        if len(q)!=0:
            print(q[0])
        else:
            print(-1)
    elif s=='back':
        if len(q)!=0:
            print(q[-1])
        else:
            print(-1)
    elif s=='size':
        print(len(q))
    elif s=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif s=='pop':
        if len(q)!=0:
            print(q.pop(0))
        else:
            print(-1)
