def solution(s):
    answer = []
    str_temp = []
    for i in s[2:-2].split("},{"):
        str_temp.append(list(map(int,i.split(","))))

    str_temp.sort(key = len)

    for i in str_temp :
        for j in i:
            if j not in answer :
                answer.append(j) 

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))