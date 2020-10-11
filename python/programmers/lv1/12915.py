# 첫번째 풀이 (sort, lambda 식 이용)
def solution(strings, n):
    answer = sorted(sorted(strings), key = lambda x: x[n])

    return answer


# 두번째 풀이 (sort함수 사용 x)
def solution1(strings, n):
    length = len(strings)
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if ord(strings[i][n]) > ord(strings[j][n]):
                strings[i], strings[j] = strings[j], strings[i]
            elif ord(strings[i][n]) == ord(strings[j][n]):
                if strings[i] > strings[j] :
                    strings[i], strings[j] = strings[j], strings[i]
    answer = strings
    
    
    return answer