# 주식 가격
from collections import deque

def solution(prices):
    answer = []
    prices = deque([i for i in prices])
    
    while(len(prices)):
        item = prices.popleft()
        cnt = 0
        for i in prices:
            if item <= i :
                cnt += 1
            else :
                cnt += 1
                break

                
        answer.append(cnt)
    
    return answer

print(solution([1,2,3,2,3]))