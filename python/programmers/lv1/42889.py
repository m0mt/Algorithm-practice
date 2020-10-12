# 첫번째 풀이 (리스트로 만들어서 풀이 완료)
def solution(N, stages):
    answer = {}
    users = len(stages)
    for i in range(1, N + 1):
        failure = 0
        fail_users = stages.count(i)
        # =================================================
        # if fail_users != 0 :
        #     for j in stages :
        #         if i <= j :
        #             users += 1
        #     failure = fail_users / users
        # users는 단계가 진행됨에 따라서 전체 인원수에서 실패 인원들이 빠져나가므로
        # for 문 단축할 수 있음
        # ================================================== 
        if fail_users != 0 :
            failure = fail_users / users
            users -= fail_users
        answer[i] = failure
    answer = sorted(answer,key = lambda x: answer[x], reverse=True)
    # ============================================
    # answer는 dictionary이므로 sorted에 answer를 그냥 넘기면 answer의 keys가 들어감. 
    # keys는 생략이 가능. 
    # 거기에 lambda는 기준을 answer[x]: 즉 value로 정렬한다는 뜻. 그래서 key가 출력
    # >>>>>>>>>>>
    # 원래 코드
    # answer = sorted(answer,key = lambda x: x[1], reverse=True)
    # answer = [i[0] for i in answer]
    # ============================================
    return answer


print(solution(5,[2,1,2,6,2,4,3,3]))
print(solution(4,[4,4,4,4,4]))