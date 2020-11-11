def solution(s):
    answer = []
    for i in s.split(' '):
        answer.append(i.capitalize())

    return ' '.join(answer)

# 코드 줄이기

def solution1(s):
    return ' '.join(i.capitalize() for i in s.split(' '))
print(solution1("3people unFollowed me"))
print(solution1("for the last week"))