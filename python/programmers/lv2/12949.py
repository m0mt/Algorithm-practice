#첫번째 풀이
def solution(arr1, arr2):
    # answer = [[0 for _ in range(width)] for _ in range(height)]
    answer = []
    for k in range(len(arr1)):
        temp_arr = []
        for i in range(len(arr2[0])):
            temp = 0 
            for j in range(len(arr1[0])):
                temp += arr1[k][j] * arr2[j][i]
            temp_arr.append(temp)
        answer.append(temp_arr)

    return answer

print(solution([[1,4],[3,2],[4,1]],[[3,3],[3,3]]))
print(solution([[2,3,2],[4,2,4],[3,1,4]],[[5,4,3],[2,4,1],[3,1,1]]))
print(solution([[1,4],[3,2],[4,1]],[[3,3,2,2],[3,3,2,2]]))