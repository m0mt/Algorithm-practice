import time
start = time.time()

n = int(input())
a = input().split( )
x , y = 1, 1

for i in range(len(a)) :
    if a[i] == 'R' and y < n :
        y = y + 1
    elif a[i] == 'L' and y > 1 :
        y = y - 1
    elif a[i] == 'U' and x > 1 :
        x = x - 1
    elif a[i] == 'D' and x < n :
        x = x + 1
end = time.time()


print(x , y)
# print('끝난시간' , end - start)