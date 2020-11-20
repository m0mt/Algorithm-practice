def solution(n, computers):
    answer = 0 
    bfs = []
    visited = [0] * n

    while 0 in visited :
        idx = visited.index(0)
        visited[idx] = 1
        bfs.append(idx)
        while bfs:
            network = bfs.pop(0)
            for i in range(n):
                if computers[network][i] == 1 and visited[i] == 0:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer

# BFS, DFS 에 대해 더욱 공부해볼것

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))