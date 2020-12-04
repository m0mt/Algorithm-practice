# 첫번째 풀이
# works의 최대값을 찾고 1씩 줄이면서
# 최소값을 찾는 방식
# index, max 함수를 while 안에 들어가서
# 시간 복잡도가 늘어남
def solution1(n, works):
    while n and sum(works) != 0:
        works[works.index(max(works))] -= 1
        n -= 1
    return sum([i ** 2 for i in works])
# 두번째 풀이
# works를 반복문을 돌릴 때 마다 sort를 해서
# 최대값에서 1씩 줄여나가는 방식
# 첫번째 방식과 거의 동일
# 시간 복잡도 오류
def solution2(n, works):
    while n and sum(works) != 0:
        works.sort()
        works[-1] -= 1
        n -= 1        
    return sum([i ** 2 for i in works])
# 세번째 풀이
# works의 총 합에서 n을 빼서
# 총 합을 골고루 나눠주는 방식
# works 1, [9,3,3]인 경우
# [8,3,3] 이 되어야 하지만 [4,5,5] 가 되므로 오류
def solution3(n, works):
    l = len(works)
    num = sum(works) - n if sum(works) > n else 0

    answer = (num // l) ** 2 * (l - (num % l)) + (num // l + 1) ** 2 * (num % l)
    return answer

# 우선순위 큐인 heapq 를 사용
# heapq 는 pop 할 때 최소값이 나오기 때문에
# heapq의 값을 음수로 만들어서 해결
def solution(n, works):
    import heapq
    if sum(works) <= n :
        return 0
    works = [(-i, i) for i in works]
    heapq.heapify(works)
    while n:
        i = heapq.heappop(works)[1] - 1
        heapq.heappush(works, (-i, i))
        n -= 1
    return sum([i[1] ** 2 for i in works])
print(solution(4,[4,3,3]))
print(solution(1,[2,1,2]))
print(solution(3,[1,1]))