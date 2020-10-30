def solution(n, words):
    answer = []
    temp = [words[0]]
    l = len(words)
    for i in range(1, l) :
        if words[i] in temp or words[i][0] != temp[-1][-1]:
            answer = [n if (i + 1) % n == 0 else (i + 1) % n, int(-(-(i + 1) // n))]
            break
        else :
            temp.append(words[i])

    if temp == words :
        answer = [0,0]

    return answer

print(solution(3,["tank","kick","know","wheel","land","dream","mother","robot","tank"]))
print(solution(5,["hello","observe","effect","take","either","recognize","encourage","ensure","establish","hang","gather","refer","reference","estimate","executive"]))
print(solution(2,["hello","one","even","never","now","world","draw"]))
