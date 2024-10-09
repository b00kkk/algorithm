#BOJ 20920
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
dic={}
for _ in range(N):
    word=input().strip()
    if len(word)<M:
        continue
    else:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1

word_list=sorted(dic.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))

for i in word_list:
    print(i[0])