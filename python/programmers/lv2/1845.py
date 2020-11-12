def solution(nums):
    answer = 0
    n = len(nums) // 2 # 개수
    temp = {}
    for i in nums:
        if i in temp:
            temp[i] += 1
        else :
            temp[i] = 1
    l = len(temp)
  
    return min(l, n)

# 두번째 풀이 
# set 함수를 이용하면 몇 종류인지 바로 구할수 있음
def solution1(nums):
    return min(len(set(nums)), len(nums) // 2)
print(solution([3,1,2,3])) #2
print(solution([3,3,3,2,2,4])) #3
print(solution([3,3,3,2,2,2])) #2