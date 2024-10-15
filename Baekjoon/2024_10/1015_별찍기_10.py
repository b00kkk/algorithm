#BOJ 2447
import sys
input=sys.stdin.readline

N=int(input())
start=['***','* *','***']

def divideAndConquer(num,star):
    if num==N:
        return star
    
    tmpStar=[]
    for i in range(num):
        tmpStar.append(star[i]*3)
    
    for i in range(num):
        tmpStar.append(star[i]+' '*num+star[i])

    for i in range(num):
        tmpStar.append(star[i]*3)
    
    return divideAndConquer(num*3,tmpStar)

result=divideAndConquer(3,start)
for i in result:
    print(i)