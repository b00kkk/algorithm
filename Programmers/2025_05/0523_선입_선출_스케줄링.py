# Programmers 12920
def solution(n, cores):
    if n<=len(cores):
        return n
    
    left,right=0,max(cores)*n
    while left<=right:
        mid=(left+right)//2
        total=sum(mid//core for core in cores)+len(cores)
        
        if total>=n:
            answer_time=mid
            right=mid-1
        else:
            left=mid+1
    
    finished=sum((answer_time-1)//core for core in cores)+len(cores)
    
    for i,core in enumerate(cores):
        if answer_time%core==0:
            finished+=1
            if finished==n:
                return i+1