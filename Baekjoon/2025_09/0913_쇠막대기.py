# BOJ 10799
import sys

batch=sys.stdin.readline().strip()

stack=[]
result=0

for i in range(len(batch)):
    if batch[i]=='(':
        stack.append('(')
    else:
        if batch[i-1]=='(':
            stack.pop()
            result+=len(stack)
        else:
            stack.pop()
            result+=1
print(result)