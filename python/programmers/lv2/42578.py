def solution(clothes):
    answer = 1 
    clothes_cnt = {}
    for i in clothes :
        if i[1] in clothes_cnt:
            clothes_cnt[i[1]] += 1
        else :
            clothes_cnt[i[1]] = 1
    clothes_cnt = list(clothes_cnt.values())
    for i in clothes_cnt:
        answer *= (i + 1)
    
    answer -= 1
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))