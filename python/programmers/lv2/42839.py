from itertools import permutations

def solution(numbers):
    answer = 0
    num = []
    _num = []
    length = len(numbers)
    #수의 모든 조합
    for i in range(1, length + 1):
        num += list(permutations(numbers, i))
    

    for i in num:
        j = int("".join(i))
        if j > 1: # 0, 1은 소수가 아니므로 제외
            _num.append(j)

    _num = list(set(_num))
    # 소수 구별 
    for i in _num:
        for j in range(2, int(i ** 0.5) + 1): #범위 
            if i % j == 0:
                answer += 1
                break

    answer = len(_num) - answer
    return answer


print(solution("17"))
print(solution("011"))