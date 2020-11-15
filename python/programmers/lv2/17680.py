from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache_hit = 1 # cache값이 있을때 추가할 시간
    cache_miss = 5 # cache값이 없을때 추가할 시간      
    # cache = deque() # deque의 maxlen =  값을 설정하면 불필요한 과정을 줄일수 있음
    cache = deque(maxlen = cacheSize)
    if cacheSize == 0:
        return len(cities) * cache_miss

    for city in cities:
        city = city.lower()

        if city in cache:
            answer += cache_hit
            cache.remove(city)
        else :
            answer += cache_miss
            # if len(cache) == cacheSize:
            #     cache.popleft()
        cache.append(city)

    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(5,["SEOUL","SEOUL","SEOUL"]))