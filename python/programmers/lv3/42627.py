def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x : x[1])
    l = len(jobs)
    t = 0
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= t:
                answer += jobs[i][1] - jobs[i][0] + t
                t += jobs[i][1]
                jobs.pop(i)
                break
        else :
            t += 1
    return answer // l
print(solution([[0,3],[1,9],[2,6]]))
# print(solution([[0,9],[0,8],[1,1],[1,1],[1,1]]))