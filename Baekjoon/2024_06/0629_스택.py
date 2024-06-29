#BOJ 10828
import sys
n=int(sys.stdin.readline())
stack=[]
for i in range(n):
    a=sys.stdin.readline().rstrip()
    if 'push' in a:
        push,a_int=a.split()
        stack.append(int(a_int))
    elif a=='size':
        print(len(stack))
    elif a=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif a=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif a=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
