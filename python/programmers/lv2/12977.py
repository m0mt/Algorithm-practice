from itertools import combinations
def solution(nums):
    answer = 0
    nums = [sum(i) for i in combinations(nums, 3)]
    for num in nums :
        for i in range(2, int(num ** 0.5) + 1) :
            if num % i == 0:
                break
        else :
            answer += 1
    return answer


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))