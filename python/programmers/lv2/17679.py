import copy
def solution(m, n, board):
    answer = 0
    board_ = []
    # 문자열 블록을 숫자 리스트 형식으로 바꿈
    for blocks in board: 
        temp = []
        for block in blocks:
            temp.append(ord(block) - 64)
        board_.append(temp)
    # 행, 열 바꿈
    board = [list(reversed(i)) for i in zip(*board_)]

    while True:
        copy_board = copy.deepcopy(board)
        s = set()
        for i in range(len(board) - 1):
            for j in range(len(board[0]) - 1):
                temp = [board[i][j], board[i][j + 1], board[i + 1][j], board[i + 1][j + 1]] 
                if temp.count(temp[0]) == 4 and temp[0] != -1:
                    s.update([(i,j),(i + 1,j),(i, j + 1),(i + 1, j + 1)])
        
        for i, j in s:
            board[i][j] = 0

        for i in board:
            cnt = 0
            while 0 in i:
                i.remove(0)
                cnt += 1
            for j in range(cnt):
                i.append(-1)
        answer += len(s)

        if copy_board == board :
            break
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
