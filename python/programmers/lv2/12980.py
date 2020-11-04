def solution(n):
    ans = 0
    battery = 0
    while n :
        if n % 2 == 0 :
            n = n / 2
        else :
            battery += 1
            n -= 1

    ans = battery
    return ans

# 다른사람의 풀이 
def solution1(n):
    return bin(n).count('1')
# 2진법이 2로 나눴을때 나오는 나머지 1,0으로 구성된 숫자들이라서
# 2진법으로 변환후 1의 개수만 세어주면 값이 나온다.
print(solution(5))
print(solution(6))
print(solution(5000))
