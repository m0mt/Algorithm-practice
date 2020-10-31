x = int(input())

dp = [0 for _ in range(x+1)]

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if not i % 2 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    if not i % 3 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
    if not i % 5 and dp[i] > dp[i//5] + 1:
        dp[i] = dp[i//5] + 1
print(dp)
print(dp[x])