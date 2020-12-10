def solution(n):
    answer = delivery(n , 1, 3, 2)
    return answer

def delivery(n, start, end, mid):
    if n == 1:
        return [[start,end]]
    return delivery(n - 1, start, mid, end) + [[start,end]] + delivery(n - 1, mid, end, start)

print(solution(2))
print(solution(3))
print(solution(4))
