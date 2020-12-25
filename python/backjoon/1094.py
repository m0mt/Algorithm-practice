x = int(input())

length = [64]

while x != 0 and x != 64:
    poll = length.pop()
    poll //= 2

    if x > poll:
        length.append(poll)
        x -= poll
    elif x == poll:
        x -= poll
    
    length.append(poll)
print(len(length))





