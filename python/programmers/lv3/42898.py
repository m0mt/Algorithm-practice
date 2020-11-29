def solution(m, n, puddles):
    dp = [[0 for i in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) == (1, 1):
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[-1][-1]

    return answer%1000000007

# 첫번째 풀이
# queue에 [1,1] 값을 집어넣고 오른쪽으로가거나 아래로 가는 방법밖에
# 없으니 이분법을 이용해서 풀이하려고함 (시간초과)
# 그리고 (m, n)으로 주어진 좌표와
# 리스트에서 [m, n]이 차이가 있음
# from collections import deque
# def solution1(m, n, puddles):
    # answer = 0
    # dp = deque([[1,1]])
    # # while dp[-1] != [m,n] and dp:
    # #     x, y = dp.popleft()
    # #     a = [x , y + 1]
    # #     b = [x + 1, y]
    # #     if a not in puddles and y + 1 <= n:
    # #         dp.append(a)
    # #     if b not in puddles and x + 1 <= m:
    # #         dp.append(b)

    # answer = len(dp)            
    # return answer % 1000000007
    # # for _ in range(m + n - 2):
    # #     temp = []
    # #     for x, y in dp :
    # #         a = [x, y + 1]
    # #         b = [x + 1, y]
    # #         if a not in puddles and y + 1 <= n:
    # #             temp.append(a)
    # #         if b not in puddles and x + 1 <= m:
    # #             temp.append(b)
    # #     dp = temp

print(solution(4,3,[[2,2]]))
    
