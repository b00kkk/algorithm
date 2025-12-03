# BOJ 2630
import sys
input=sys.stdin.readline

n=int(input())
square=[]
for i in range(n):
    square.append(list(map(int,input().split())))
color_list=[]
def f(x,y,n):
    paper_color=square[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper_color!=square[i][j]:
                f(x,y,n//2)
                f(x,y+n//2,n//2)
                f(x+n//2,y,n//2)
                f(x+n//2,y+n//2,n//2) 
                return
    if paper_color==0:
        color_list.append(0)
    else:
        color_list.append(1)
f(0,0,n)
print(color_list.count(0))
print(color_list.count(1))