#첫번째 풀이 (효율성 테스트 시간초과)
def solution1(s):
    answer = 0
    prev = ""
    i = 0
    while i < len(s):
        temp = s[i : i + 1]
        if prev == temp:
            s = s[: i - 1] + s[i + 1 :]
            i -= 1
            prev = s[i - 1 : i]
        else : # 앞뒤가 다를 때
            prev = temp
            i += 1 
    if not s :
        answer = 1        
    return answer

#두번째 풀이 (리스트로 풀이)
def solution(s):
    answer = 0 
    stack = []

    for i in s:
        if not stack:
            stack.append(i)
        else :
            if stack[-1] == i :
                stack.pop()
            else :
                stack.append(i)
        
    if not stack:
        answer = 1
    return answer


print(solution("baabaa"))
print(solution("cdcd"))