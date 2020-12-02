INF = 100000000
number = 4

a = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]
def floydWarshall(a):
    # 거쳐 갔을때 비용이 더적을 경우
    # 최소비용으로 교체하는 알고리즘
    # k = 거쳐가는 노드
    for k in range(number):
        # i = 출발 노드
        for i in range(number):
            if k == i : # 거쳐가는 노드와 출발 노드가 겹쳐지는 부분은 바꿀 필요가 없음
                continue
            # j = 도착 노드
            for j in range(number):
                if i == j : # k == i 와 마찬가지
                    continue
                if a[i][k] + a[k][j] < a[i][j] :
                    a[i][j] = a[i][k] + a[k][j]
    return a
print(floydWarshall(a))
