def solution(N, number):
    dp = [0, [N]]
    if number == N: # 없어도 동작은 됨
        return 1

    for k in range(2, 9):
        temp = set()
        for l in range(1, k // 2 + 1):
            for i in dp[l]:
                for j in dp[k - l]:
                    temp.add(i + j)
                    temp.add(i - j)
                    temp.add(j - i)
                    temp.add(i * j)
                    temp.add(int(str(N)*k))
                    if i != 0:
                        temp.add(j // i)
                    if j != 0:
                        temp.add(i // j)
        if number in temp:
            return k
        dp.append(list(temp))
    return -1
# 알고리즘 풀 때 규칙부터 천천히 찾을 것 
# 풀어보려고 하면 다풀림
# 작은 것 부터 -> 큰 것으로 * 특히 DP 문제
print(solution(5, 12))
print(solution(2, 11))
