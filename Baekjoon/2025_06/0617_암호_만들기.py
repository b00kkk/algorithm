# BOJ 1759
import sys
from itertools import combinations
input = sys.stdin.readline

L,C=map(int,input().split())
s=list(input().split())
s.sort()

vowel = {'a','e','i','o','u'}

for i in combinations(s,L):
    voewl_count = sum(1 for ch in i if ch in vowel)
    consonant_count = L-voewl_count
    if voewl_count>=1 and consonant_count>=2:
        print(''.join(i))