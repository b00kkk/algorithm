#BOJ 2877
import sys
from itertools import product
input = sys.stdin.readline

K=int(input())
K=bin(K+1)[3:]

print(K.replace('0','4').replace('1','7'))