point = tuple(map(int, input().split()))

def solution(point):
    ax = point[0] - point[2]
    ay = point[1] - point[3]
    bx = point[0] - point[4]
    by = point[1] - point[5]
    cx = point[2] - point[4]
    cy = point[3] - point[5]
    # 한 직선위에 3개의 점이 같이 있는 경우
    if 0 in (ax, bx, cx):
        if ax == bx == cx:
            return -1
    else :
        if ay / ax == by / bx == cy / cx:
            return -1
    a = ((ax ** 2) + (ay ** 2)) ** (1 / 2)
    b = ((bx ** 2) + (by ** 2)) ** (1 / 2)
    c = ((cx ** 2) + (cy ** 2)) ** (1 / 2)
    answer = max(a, b, c) * 2 - min(a, b, c) * 2
    return answer

print(solution(point)) 