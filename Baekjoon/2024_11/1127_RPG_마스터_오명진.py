#BOJ 22941
import sys
import math
input=sys.stdin.readline

HP1,ATK1,HP2,ATK2=map(int,input().split())
P,S=map(int,input().split())

if HP2 - (math.ceil(HP2/ATK1)-1) * ATK1 >P:
    R2=math.ceil(HP2/ATK1)
else:
    R2=math.ceil((HP2+S)/ATK1)

R1=math.ceil(HP1/ATK2)
if R1>=R2:
    print("Victory!")
else:
    print("gg")