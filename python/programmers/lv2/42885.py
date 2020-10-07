def solution(people, limit):
    answer = 0
    people.sort()
    
    ## 첫번째 풀이 방법
    ## people 배열 정렬 한 뒤 왼쪽 pop 오른쪽 pop 해서 값 비교 해서 넣을 것 
    ## pop과 for문에 의해 효율성 테스트 실패
    # while people :
    #     weight_limit = limit
    #     weight_limit -= people.pop()
    #     for i in people:
    #         if(weight_limit >= i):
    #             weight_limit -= people.pop(people.index(i))
    #             break

    #     answer += 1

    # 두번째 풀이
    # 무거운 사람과 가벼운 사람 합이 limit 초과 할시 같이 태워보내고
    # 아니면 무거운 사람만 태워 보낼 것 
    i = 0
    j = len(people) - 1
    while i <= j :
        if i != j:
            if people[i] + people[j] <= limit:
                i += 1
        j -= 1
        answer += 1
    return answer 
    





print('1', solution([70,50,80,50],100))
print('2', solution([70,80,50],100))
print('3', solution([20,20,30,80],100))