def solution(n):
    answer = [[0 for _ in range(i)] for i in range(1, n + 1)] 
    all = 0
    for i in range(n):
        all += i + 1
    idx = 0
    floor = 0
    flag = True # 방향
    i = 1
    while i < all + 1:
        answer[floor][idx] = i 
        if flag : 
            if floor != n - 1 : #맨 아랫줄이 아닐때 층수 하강 
                floor += 1
            else : #맨 아랫줄일 때
                if 0 not in answer[n - 1] : # 층수 상승
                    flag = False
                    n = n - 1
                    idx -= 1
                    floor -= 1
                else :
                    idx += 1
        else :
            if 0 not in answer[floor] :
                flag = True
                floor += 1
            else :
                floor -= 1
                idx -= 1
        i += 1
    answer = sum(answer, [])
    return answer

print(solution(6))