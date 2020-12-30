from itertools import combinations
n, m = map(int, input().split())
data = map(int, input().split())
def solution(n, m, data):
    result = 0
    for i in set(map(sum,combinations(data, 3))) :
        if result <= i <= m :
            result = i
    return result

print(solution(n, m, data))