# 첫번째 풀이
# while 문 두개를 써서 abba의 경우와 
# ababa의 경우로 나눠서 풀이함
def solution1(s):
    answer = 0
    n = len(s)
    for i in range(n):
        t = 1
        while i - t >= 0 and i + t < n:
            if s[i - t] == s[i + t]:
                t += 1
            else :
                break
        if answer < (t - 1) * 2 + 1:
            answer = (t - 1) * 2 + 1
        t = 1
        while i - t >= 0 and i + t - 1 < n:
            if s[i - t] == s[i + t - 1]:
                t += 1
            else :
                break
        if answer < (t - 1) * 2:
            answer = (t - 1) * 2
    return answer

# 두번째 풀이
# [::-1] 를 이용하면 문자열을 뒤집을수 있는데
# 계속 해서 뒤집어서 확인하는 방식
# 시간 오래걸림
def solution(s):
    answer = 0 
    n = len(s)
    for i in range(n):
        for j in range(i, n + 1):
            string = s[i:j]
            if string == string[::-1]:
                length = len(string)
                if answer < length:
                    answer = length
    return answer
print(solution("a"))
# print(solution("abacde"))
# print(solution("babcedecbadad"))
# print(solution("aba"))
# print(solution("abde"))