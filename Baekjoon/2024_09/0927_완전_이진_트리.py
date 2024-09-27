#BOJ 9934
import sys
input = sys.stdin.readline

K=int(input())
b=list(map(int,input().split()))
tree=[[] for _ in range(K+1)]

def find_root(step,start,end):
    if step == 0:
        return
    root_idx = start+ 2 ** (step - 1) - 1
    tree[step].append(b[root_idx])
    # 루트 노드의 전 후로 범위를 반으로 줄여 재귀를 돌린다
    find_root(step-1, start, root_idx-1)
    find_root(step - 1, root_idx +1, end)

find_root(K,0,len(b))
for i in range(K,0,-1):
    print(*tree[i])