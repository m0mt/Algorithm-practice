n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(input())

answer = 64
x = 0 
y = 0
for x in range(n - 8 + 1):
    for y in range(m - 8 + 1):
        cnt = 0
        start = "W" 
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if j % 2 == 0 and array[i][j] != start:
                    cnt += 1
                if j % 2 == 1 and array[i][j] == start:
                    cnt += 1
            if start == "W" : start = "B"
            else : start = "W"
        answer = min(answer, cnt, 64 - cnt)
print(answer)