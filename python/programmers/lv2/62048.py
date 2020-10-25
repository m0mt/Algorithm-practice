import math

def solution(w,h):
    ## (-(-l // s)) 기울기를 구하는 값인데 구했을 시 가로 1칸에 세로 몇칸을
    ## 지나가는지 알 수 있다.
    ## 되지 않는 이유를 찾을 것, 최대 공약수 공식이 나오게 된 이유를 알아 볼 것

    # all_count = w * h

    # if w > h:
    #     l = w
    #     s = h
    # else :
    #     l = h 
    #     s = w
    # white_square = (-(-l // s)) * s
    # answer = all_count - white_square
    # return answer
    all_count = w * h
    white_square = w + h - math.gcd(w,h)
    answer = all_count - white_square
    return answer

print(solution(8,12))