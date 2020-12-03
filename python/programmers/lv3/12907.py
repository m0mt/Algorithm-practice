# 다른 사람의 풀이
# DP 알고리즘
# 표를 그려서 규칙을 파악하는데 어려움이 있음.
# 더 알아볼 것
def solution(n, money):
    dp = [1] + [0] * n

    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                dp[price] += dp[price - coin]
    
    return dp[n] % 1000000007

print(solution(5, [1,2,5]))