a, b = map(int, input().strip().split(' '))
str = ''
for _ in range(b):
    for _ in range(a):
        str += '*'
    str += '\n'
print(str)