# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
def solution(n):
    i = n + 1
    n_cnt = bin(n).count("1")
    i_cnt = bin(i).count("1")
    while n_cnt != i_cnt:
        i += 1
        i_cnt = bin(i).count("1")
    answer = i
    return answer


print(solution(78))
print(solution(15))