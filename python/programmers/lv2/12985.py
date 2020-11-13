def solution(n,a,b):
    answer = 0
    while a != b:
        a = -(- a // 2)
        b = -(- b // 2)
        answer += 1
    return answer

print(solution(8,4,7))