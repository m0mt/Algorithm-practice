L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())
a = 1 
b = 1
if n in S:
    print(0)
else :
    answer = 0
    for i in S:
        if i < n :
            a = i + 1
        else :
            b = i - 1
            break
    a = n - a
    b = b - n
    answer = a + b + (a * b)
    print(answer)