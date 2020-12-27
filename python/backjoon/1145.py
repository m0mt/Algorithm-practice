num = list(map(int, input().split()))
n = len(num)
answer = 10000000
def gcd(a, b):
    result = 1
    while True:
        for i in range(2, min(a, b) + 1):
            if a % i == b % i == 0:
                a = a // i
                b = b // i
                result *= i
                break
        else :
            return result

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            _gcd = gcd(num[i], num[j])
            temp = num[i] * num[j] // _gcd
            _gcd = gcd(temp, num[k])
            temp = temp * num[k] // _gcd
            answer = min(answer, temp)

print(answer)
