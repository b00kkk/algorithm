# BOJ 1992
import sys
input=sys.stdin.readline

N=int(input())
image=[input() for _ in range(N)]
answer=""

def comp(x,y,N):
    check= image[x][y]
    global answer
    for row in range(x,x+N):
        for col in range(y,y+N):
            if check!=image[row][col]:
                answer+='('
                comp(x,y,N//2)
                comp(x,y+N//2,N//2)
                comp(x+N//2,y,N//2)
                comp(x+N//2,y+N//2,N//2)
                answer+=')'
                return None
    if check=='0':
        answer+='0'
    else:
        answer+='1'
    return None

comp(0,0,N)
print(answer)