#BOJ 2108
import sys
n=int(sys.stdin.readline())
n_list=[]
for i in range(n):
    a=int(sys.stdin.readline())
    n_list.append(a)
if int(sum(n_list)/len(n_list)+0.5)>=0:
    print(int(sum(n_list)/len(n_list)+0.5))
else:
    print(int(sum(n_list)/len(n_list)-0.5))
n_list.sort()
print(n_list[len(n_list)//2])
mode={}
for i in n_list:
    if i in mode:
        mode[i]+=1
    else:
        mode[i]=1
mode_key=[]
for k,v in mode.items():
    if v==max(mode.values()):
        mode_key.append(k)
mode_key.sort()
if len(mode_key)>1:
    print(mode_key[1])
else:
    print(mode_key[0])
print(max(n_list)-min(n_list))