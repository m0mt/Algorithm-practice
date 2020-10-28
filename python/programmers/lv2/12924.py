#첫번째 풀이
# dfs함수를 돌렸을 때 
def solution1(n):
    answer = 0
        
    def dfs(start, temp):
        if sum(temp) < n:
            temp.append(start)
            dfs(start + 1, temp)
        elif sum(temp) == n:
            nonlocal answer
            answer += 1
            return
    
    for i in range(1, n + 1):
        temp = []
        dfs(i, temp)

    return answer

#두번째 풀이 
# 반복문으로 풀이
def solution(n) :
    answer = 0 
    temp = 0
    for i in range(1, n + 1):
        temp = 0
        while True:
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
            temp += i
            i += 1
    return answer

print(solution(15))


