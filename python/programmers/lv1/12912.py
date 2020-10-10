# 첫번째 풀이 방법 
def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    
    while a <= b:
        answer += a
        a += 1
        
    return answer

# 두번째 풀이 방법 (배열 이용해서 풀이)
# 시간이 좀더 걸린다.
def solution1(a, b):
    if a > b:
        a, b = b, a
    number = [i for i in range(a, b + 1)]

    answer = sum(number)
    return answer 
