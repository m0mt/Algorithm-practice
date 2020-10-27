# 첫번째 풀이 
def solution(numbers, target):
    answer = 0 
    array = [0]
    for number in numbers:
        sub_array = []
        for result in array :
            sub_array.append(result + number)
            sub_array.append(result - number)
        array = sub_array

    return array.count(target)


    

print(solution([1,1,1,1,1],3))
# print(solution([1,1,1,1,2],4))
# print(solution([1,1,1,1,1,1,1],3))