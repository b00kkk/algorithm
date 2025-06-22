# BOJ 1475
import sys
input = sys.stdin.readline

N=input().strip()
dict={'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}
for i in N:
    if i=='9':
        dict['6']+=1
    else:
        dict[i]+=1
if dict['6']%2==1:
    dict['6']+=1
dict['6']=dict['6']//2
print(max(dict.values()))