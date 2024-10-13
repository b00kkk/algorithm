#BOJ 4779
import sys
input=sys.stdin.readline

def cantor(s):
    if s=='-':
        return '-'
    cantor_s=s[:len(s)//3]
    cantor_s=cantor(cantor_s)
    s=cantor_s+' '*(len(s)//3)+cantor_s
    return s

while True:
    try:
        N=int(input())
        s='-'*(3**N)
        s=cantor(s)
        print(s)
    except:
        break