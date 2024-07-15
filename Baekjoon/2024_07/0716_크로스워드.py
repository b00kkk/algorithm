#BOJ 1706
import sys
r,c=map(int,sys.stdin.readline().split())
puzzle=[]
arr={i: '' for i in range(c)}
for i in range(r):
    s=sys.stdin.readline().strip()
    for word in s.split('#'):
        if len(word)>1:
            puzzle.append(word)
    for j in range(c):
        arr[j]+=s[j]

for j in range(c):
    s=arr[j]
    for word in s.split('#'):
        if len(word)>1:
            puzzle.append(word)

puzzle.sort()
print(puzzle[0])