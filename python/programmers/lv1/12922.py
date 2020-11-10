def solution(n):
    answer = '수박' * (n // 2) + '수' if not n % 2 == 0 else '수박' * (n // 2)
    return answer

def solution1(n):
    answer = '수박' * (n // 2) + '수' * (n % 2)
    return answer 