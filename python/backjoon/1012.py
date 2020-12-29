import sys
# 재귀가 깊어서 런타임 에러가 발생할수 있으니 재귀깊이를 설정해주는 코드
sys.setrecursionlimit(10000) 
T = int(input())
answer = []
def dfs(x, y, field):
    if x < 0 or y > M - 1 or y < 0 or x > N - 1:
        return False

    if field[x][y] == 1:
        field[x][y] = 0
        dfs(x - 1, y, field)
        dfs(x, y - 1, field)
        dfs(x + 1, y, field)
        dfs(x, y + 1, field)
        return True
    return False

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]* M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        a, b = map(int, input().split())
        field[b][a] = 1

    for i in range(N):
        for j in range(M):
            if dfs(i, j, field) == True:
                cnt += 1
    print(cnt)