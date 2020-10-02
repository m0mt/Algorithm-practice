def solution(priorities, location):
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
    print(final_location)
    return answer

print(solution(	[1, 1, 9, 1, 1, 1], 0))