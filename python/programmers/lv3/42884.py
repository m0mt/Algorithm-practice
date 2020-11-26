def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[0])
    left, right = routes.pop()
    while routes:
        a, b = routes.pop()
        if b >= left:
            right = b if b < right else right
        else :
            answer += 1
            left, right = a, b
    answer += 1
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))