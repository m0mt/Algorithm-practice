def solution1(scoville, K):

    # 첫번째 풀이 (시간초과)
    answer = 0
    while True :
        scoville.sort(reverse = True)
        x = scoville.pop()
        if x > K :
            break
        y = scoville.pop()
        
        x = x + (y * 2)
        
        if x < K and not scoville :
            answer = -1
            break
        scoville.append(x)
        answer += 1
    return answer

import heapq

def solution(scoville, K):
    # 두번째 풀이 (heapq 라이브러리 사용)
    answer = 0
    heap = []
    for i in scoville :
        heapq.heappush(heap, i)

    while heap[0] < K :
        x = heapq.heappop(heap)
        if heap :  
            y = heapq.heappop(heap)
            heapq.heappush(heap, x + (y * 2))
            answer += 1
        else :
            answer = -1
            break
    return answer    

print(solution([1,2,3,9,10,12], 7))