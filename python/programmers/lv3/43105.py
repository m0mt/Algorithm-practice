#첫번째 풀이
def solution(triangle):
    dp = []
    for lst in triangle:
        if not dp :
            dp.append(lst[0])        
            continue

        temp = [0]

        for i in range(len(dp)):
            temp.append(max((dp[i] + lst[i]), temp.pop()))
            temp.append(dp[i] + lst[i+1])
        dp = temp
    return max(dp)

# 두번째 풀이
# 위와 방식은 같음
def solution1(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][0] += triangle[i-1][0]
            elif j == i:
                triangle[i][-1] += triangle[i-1][-1]
            else :
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]) 
    return max(triangle[-1])
# 리스트 [3,8] 부터 시작해서 계속 더해가는 방식
# [8,1,0] 에서 1은 3,8인 선택지가 나오는데 max 로 판별

print(solution1([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))