def solution(s):
    number = list(map(int,s.split(" ")))
    answer = str(min(number)) + ' ' + str(max(number))  
    
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))