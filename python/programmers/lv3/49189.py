from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    dists = {i : 0 for i in range(1, n + 1)}
    distance = 1

    for a, b in edge:
        graph[b].append(a)
        graph[a].append(b)
    queue = deque(graph[1])

    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()
            if dists[v] == 0:
                dists[v] = distance
                for j in graph[v]:
                    queue.append(j)
        distance += 1
    dists[1] = 0
    return list(dists.values()).count(max(dists.values()))



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))