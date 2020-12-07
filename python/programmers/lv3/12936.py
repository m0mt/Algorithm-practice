def solution(n, k):
    answer = []
    num = [i + 1 for i in range(n)]
    factorial = 1
    for i in range(2,n + 1):
        factorial *= i
    while n:
        factorial = factorial // n
        # temp = k // factorial if k % factorial != 0 else k // factorial -1
        # k - 1 을 했을경우 위 경우처럼 if 문을 쓰지 않아도 됨
        temp = (k - 1) // factorial
        # 나머지 구하는 부분도 안쓰는 방법 찾아볼 것
        # k = k % factorial 라고만 했을때 나머지가 0 인수는
        # 다음 temp 값이 -1로 되어서 마지막 수 가 뽑히게 된다.
        # 정확한 인덱스값이 나오게 하려고 한다면 아래를 주석을 이용
        k = k % factorial if k % factorial != 0 else factorial
        answer.append(num[temp])
        num.pop(temp)
        n -= 1
    return answer
print(solution(4,12))