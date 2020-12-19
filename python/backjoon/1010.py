T = int(input())
array = []
for _ in range(T):
    array.append(list(map(int, input().split())))

for n, m in array:
    a = 1
    b = 1
    for i in range(m - n + 1, m + 1):
        a *= i
    for j in range(1, n + 1):
        b *= j
    print(a//b)
