# 첫번째 풀이 
import heapq
def solution1(genres, plays):
    answer = []
    # 장르별 재생수에 따라 순위 설정 
    genres_dict = {}
    for i in range(len(genres)):
        if genres[i] in genres_dict:
            genres_dict[genres[i]][0] += [i]
            genres_dict[genres[i]][1] += plays[i]
        else:        
            genres_dict[genres[i]] = [[i], plays[i]]
    s_dict = sorted(genres_dict.values(), key = lambda x : x[1], reverse=True)
    # 장르안에서 1,2등 뽑아서 (곡이 1개일 경우 1개만 택) 리스트에 추가
    for i in s_dict:
        prime = []
        for j in i[0]:
            heapq.heappush(prime, (-plays[j], j))            
        answer.append(heapq.heappop(prime)[1])
        if prime: answer.append(heapq.heappop(prime)[1])
    return answer

# 다른 풀이
def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])
    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])
# 내 풀이와 다르게 genres_dict 에 각 노래의 재생수를 모두 담고
# 각 장르의 재생수 합을 다른 리스트에 담아서 풀이
    genres_list.sort(key=lambda x: x[1], reverse=True)

    answer = []
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])) #[4,1,3,0]
print(solution(["classic","classic","classic","classic","pop"],[500,150,800,800,2500]))