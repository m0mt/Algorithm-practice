#첫번째 풀이
def solution(citations):
    answer = 0
    h_index = len(citations)
    while h_index > 0:
        cnt = 0
        for i in citations:
            if h_index <= i:
                cnt += 1
        if h_index <= cnt :
            answer = h_index
            break
        h_index -= 1

    return answer
## 문제 이해를 제대로 하지 못해서 코드가 길어짐
## 규칙을 찾는것을 습관화 할 것
# h의 최대값은 citations 의 크기 넘을수 없음

print(solution([5, 3, 6, 1, 5]))
print(solution([5, 4, 6, 1, 5]))
print(solution([2, 1, 7, 4, 8]))