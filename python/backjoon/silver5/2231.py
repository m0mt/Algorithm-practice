N = int(input())   

def solution(N):
    for i in range(1, N + 1):
        result = 0 
        result += i
        for j in str(i):
            result += int(j)
        if result == N:
            return i
    return 0

print(solution(N))