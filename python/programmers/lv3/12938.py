def solution(n, s):
    if n > s:
        return [-1]
    j = s % n    
    answer = [s // n] * (n - j) + [(s // n) + 1] * j
    return answer 
    # for i in range(n-j, n):
    #     answer[i] += 1 
    

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))
print(solution(3, 6)) # [2,2,2]
print(solution(3, 8)) # [4,2,2] < [3,3,2] 
