n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
A = numbers[0] * numbers[-1]
print(A)
