def solution(n, costs):
    answer = 0 
    costs.sort(key = lambda x: x[2])
    visited = [0] * n
    visited[0] = 1
    while 0 in visited:
        for cost in costs:
            a, b, c = cost
            if visited[a] != visited[b]:
                visited[a] = 1
                visited[b] = 1
                answer += c
                break
    return answer 


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,1]]))