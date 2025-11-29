# BOJ 1780
import sys
input=sys.stdin.readline

def solution(N, graph):
    answer = {-1: 0, 0: 0, 1: 0}

    def check(x, y, N):
        std = graph[y][x]
        for ny in range(y,y+N):
            for nx in range(x,x+N):
                if std != graph[ny][nx]:
                    return False
        return True

    def divideConquer(x, y, N):
        if check(x, y, N):
            answer[graph[y][x]] += 1
            return
        N//=3
        for dy in range(3):
            for dx in range(3):
                divideConquer(x+N*dx, y+N*dy, N)

    divideConquer(0, 0, N)

    return answer.values()

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

result = solution(N, graph)
for res in result:
    print(res)