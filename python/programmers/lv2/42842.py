def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            j = yellow // i
            if brown + yellow == (j + 2) * (i + 2):
                # brown - 4 는 모퉁이 개수를 뺀 나머지 수
                # 그러므로 i * 2 + j * 2 = brown - 4 성립
                answer.append(j + 2)
                answer.append(i + 2)
    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))

