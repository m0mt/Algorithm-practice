## 첫번째 풀이 (DP로 풀이)
def solution1(n):
    dp = [0,1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    answer = dp[-1] % 1234567

    return answer


## 두번쨰 풀이 (변수로만 풀이)
# DP로 풀이 했을 때 보다 시간이 더빠름
def solution(n):
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    answer = b % 1234567
    return answer
print(solution(3))
print(solution(5))