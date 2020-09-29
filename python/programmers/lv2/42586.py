import math

def solution(progresses, speeds):
    answer = []
    temp = math.ceil((100 - progresses[0]) / speeds[0])
    for i in range(len(progresses)) :
        curVal = math.ceil((100 - progresses[i]) / speeds[i])
        #(-(-a // b))처럼 쓰면 math.ceil 안쓰고 가능하다.
        if i == 0 or curVal > temp :
            temp = curVal
            answer.append(1)        
        else :
            answer[-1] += 1
        
                    
     
    
    return answer  



print(solution([93, 30, 55],[1, 30, 5]))