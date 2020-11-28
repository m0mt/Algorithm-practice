def solution(tickets):
    tickets.sort(key = lambda x: x[1], reverse = True)
    path = {}
    for start, end in tickets:
        path[start] = path.get(start, []) + [end]
    answer = []
    stack = ["ICN"]
    # 백트레싱 dfs 이용
    # answer 리스트에 path 에 없는 값을 넣고
    # stack 에는 진행 되는값을 넣는다.
    while stack:
        last = stack[-1]
        if last not in path or len(path[last]) == 0:
            answer.append(stack.pop())
        else :
            stack.append(path[last].pop())
    return answer[::-1]



# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))
# print(solution([["ICN","A"],["ICN","A"],["A","ICN"]]))