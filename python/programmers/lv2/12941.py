def solution(A,B):
    answer = 0
    n = len(A)
    A.sort(reverse = True)
    B.sort()
    for i in range(n):
        answer += A[i] * B[i]
    return answer

# zip 함수를 이용하면 리스트 2개를 곱할수 있음
def solution1(A,B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse= True)))

print(solution([1,4,2],[5,4,4]))
print(solution([1,2],[3,4]))