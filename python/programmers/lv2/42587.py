def solution(priorities, location):
    ## 처음 풀이 방법
    index_location = [i for i in range(len(priorities))]
    final_location = []
    
    while len(priorities):
        max_prirority = max(priorities)
        current_priority = priorities.pop(0)

        if current_priority == max_prirority:
            final_location.append(index_location.pop(0))

        else :
            priorities.append(current_priority)
            index_location.append(index_location.pop(0))
    
    answer = final_location.index(location) + 1

    ## deque 라이브러리 사용시 리스트의 .pop과 .popleft()의 
    ## 시간 복잡도 차이가 난다. 

    ## enumerate 사용해서 index값과 같이 저장
    # priorities = [[i,v] for i, v in enumerate(priorities)]
    return answer
    
print(solution([1, 1, 9, 1, 1, 1], 0))