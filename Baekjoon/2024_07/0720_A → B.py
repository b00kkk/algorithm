#BOJ 16953
import sys
a,b=map(int,sys.stdin.readline().split())

def result(a, b):
    c=0
    
    while b > a:
        if b % 2 == 0:
            b //= 2
        elif str(b)[-1] == '1':
            b = int(str(b)[:-1])
        else:
            return -1
        c += 1
    
    return c+1 if b == a else -1

print(result(a,b))