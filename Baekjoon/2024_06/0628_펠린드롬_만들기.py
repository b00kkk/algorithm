#BOJ 1213
import sys
a=sys.stdin.readline().strip()
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

odd=0
for key in dic:
    if dic[key]%2!=0:
        odd+=1

if odd>1:
    print("I'm Sorry Hansoo")
else:
    dic=sorted(dic.items())
    x=''
    y=''
    for key,values in dic:
        while values>=2:
            x+=key
            values-=2
        if values==1:
            y+=key
    print(x+y+x[::-1])
