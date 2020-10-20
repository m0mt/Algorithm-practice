def solution(board):
    width = len(board[0])
    height = len(board)

    for y in range(height - 1):
        for x in range(width - 1):
            if board[y][x] > 0:
                _min = min(board[y + 1][x + 1], board[y][x + 1], board[y + 1][x])
                r = min(board[y][x], board[y][x + 1], board[y + 1][x])
                ## y + 1, x + 1 -> y - 1, x - 1 식으로 바꿔서 사용하면 더 깔끔하게 코드 정리 가능
                ## (0, 0) ~ (2, 2) 까지 (현재 코드) 
                ## (1, 1) ~ (3, 3) 부터 시작하는 코드 (더 깔끔하게 가능) 
                if _min != 0:
                    board[y + 1][x + 1] = r + 1

    return max(map(max, board)) ** 2
        
    

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,1,1,1],[1,1,0,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))