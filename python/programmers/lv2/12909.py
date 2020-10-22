# 첫번째 풀이 
def solution(s):
    l_cnt = 0
    r_cnt = 0
    flag = True
    for i in s:
        if i == "(" :
            l_cnt += 1
        else :
            if flag == True:
                return False
            r_cnt += 1

        flag = False
        if l_cnt == r_cnt :
            flag = True
        
    if l_cnt != r_cnt :
        return False
        
    return True

# 두번째 풀이 (코드 줄이기)

def solution1(s):
    cnt = 0
    for i in s :
        cnt = cnt + 1 if i == "(" else cnt - 1

        if cnt < 0:
            return False


    return cnt == 0
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))