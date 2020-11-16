def solution(msg):
    answer = []
    dictionary = {chr(i): i - 64 for i in range(ord('A'), ord('Z') + 1)}
    temp = ""

    for i in msg:
        temp += i
        if temp not in dictionary :
            dictionary[temp] = list(dictionary.values())[-1] + 1
            answer.append(dictionary[temp[:-1]])
            temp = temp[-1]
    if temp :
        answer.append(dictionary[temp])
    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))