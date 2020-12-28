N, K = map(int, input().split())

num = [i for i in range(1, N + 1)]
result = []

# pop 을 이용한 방법(통과 완료)
# idx = K - 1
# while True:
#     result.append(str(num.pop(idx)))
#     N -= 1
#     if N == 0 : break
#     idx = (idx + K - 1) % N

# 코드 정리
idx = 0
while N:
    idx = (idx + K - 1) % N
    result.append(str(num.pop(idx)))
    N -= 1

print('<', ", ".join(result), '>', sep='')