# BOJ 5212
import sys
input=sys.stdin.readline

R,C=map(int,input().split())
m=['.'*(C+2)]
for _ in range(R):
    m.append('.'+input().strip()+'.')

m.append('.'*(C+2))
new=[list(row) for row in m]


dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(R+2):
    for j in range(C+2):
        if m[i][j]=='X':
            cnt=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if m[nx][ny]=='.':
                    cnt+=1
            if cnt>=3:
                new[i][j]='.'

rows, cols = len(new), len(new[0])
row_idx = [i for i in range(rows) if any(ch != '.' for ch in new[i])]
col_idx = [j for j in range(cols) if any(new[i][j] != '.' for i in range(rows))]

if not row_idx or not col_idx:
    pass
else:
    r1, r2 = min(row_idx), max(row_idx)
    c1, c2 = min(col_idx), max(col_idx)

    for i in range(r1, r2+1):
        print(''.join(new[i][c1:c2+1]))