# Programmers 12951
def solution(s):
    s=s.lower()
    s=' '+s
    answer=''
    for i in range(1,len(s)):
        if s[i-1]==' ':
            answer+=s[i].upper()
        else:
            answer+=s[i]
    return answer