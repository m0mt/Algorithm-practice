# 첫번째 풀이
# heap 을 사용하지 않고 queue를 수시로 정렬해서조작
# 시간오래걸림 (통과는 o)
def solution1(operations):
    operations = [i.split(" ") for i in operations]
    queue = []
    for oper, num in operations:
        num = int(num)
        if oper == "I":
            queue.append(num)
        elif oper == "D":
            if not queue:
                continue
            if num == -1:
                queue.sort(reverse=True)
                queue.pop()
            elif num == 1:  
                queue.sort()
                queue.pop()
    queue.sort()    
    answer = [queue[-1] , queue[0]] if queue else [0,0]
    return answer

# 두번째 풀이
# 우선순위 큐문제를 heap으로 이용 하기 위해
# max, min heap 두가지로 나누었다
# 나누었을때 문제는 D 1 일 때 max_heap 의 값을 min_heap에도 지워야 한다.(동기화)
def solution(operations):
    import heapq
    operations = [i.split(" ") for i in operations]
    max_heap = []
    min_heap = []
    for oper, num in operations:
        num = int(num)
        if oper == "I":
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif oper == "D":
            if num == 1:
                if max_heap == []:
                    continue
                heapq.heappop(max_heap)
                # 동기화 하는 조건
                if not max_heap or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
            else :
                if min_heap == []:
                    continue
                heapq.heappop(min_heap)
                # 동기화 하는 조건
                if not min_heap or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)] if min_heap else [0,0]
print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))