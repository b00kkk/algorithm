#BOJ 9273
import sys
input=sys.stdin.readline

while True:
    try:
        _,n=map(int,input().split('/'))
        c=0
        k=n**2
        for d in range(1,int(k**0.5)+1):
            if k%d==0:  
                x=d+n
                y=(k//d)+n
                if x<=y:
                    c+=1
        print(c)
    except:
        break