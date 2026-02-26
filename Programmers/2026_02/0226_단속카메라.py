# Programmers 42884
def solution(routes):
    routes.sort(key=lambda x:x[1])
    cam = -30001
    cctv=0
    for s,e in routes:
        if s>cam:
            cctv+=1
            cam=e
    
    return cctv