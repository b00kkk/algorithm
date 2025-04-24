# Programmers 12904

def solution(s):
    cnt=1
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            test=s[i:j]
            if test==test[::-1]:
                if cnt<len(test):
                    cnt=len(test)

    return cnt
