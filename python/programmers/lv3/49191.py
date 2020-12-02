# 플로이드 와샬 알고리즘으로 해결한 풀이
def solution1(n, results):
    answer = 0
    graph = [[0 for _ in range(n)] for _ in range(n)]
    # win: 1, lose: -1
    for win, lose in results:
        graph[win-1][lose-1] = 1
        graph[lose-1][win-1] = -1

    # k 거쳐가는 노드
    for k in range(n):
        # i 시작노드
        for i in range(n):
            # j 도착 노드
            # if k == i :
            #     continue
            for j in range(n):
                # if i == j :
                #     continue
                if graph[i][k] * graph[k][j] == 1:
                    graph[i][j] = graph[i][k]
    for person in graph:
        if person.count(0) == 1:
            answer += 1
    return answer

# 두번째 풀이
def solution(n, results):
    answer = 0 
    win, lose = {i : set() for i in range(1, n + 1)}

    for result in results:
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])

    for i in range(1, n + 1):
        # lose 함수에 집어넣을시
        # lose의 set 값이 변하게 되어 반복문 오류 발생함
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(loser[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))