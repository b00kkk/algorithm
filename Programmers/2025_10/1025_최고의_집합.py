# Programmers 12938
def solution(n, s):
    if n>s:
        return [-1]
    answer = []
    num=s//n
    for _ in range(n):
        answer.append(num)
    if num*n!= s:
        minus=s-(num*n)
        for i in range(minus):
            answer[-i]+=1
    answer.sort()
    
    
    return answer

