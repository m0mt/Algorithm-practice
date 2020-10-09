def solution(name):
    joystick = [min(ord(a) - ord('A'),ord('Z') - ord(a) + 1) for a in name]
    cnt = 0
    answer = 0
    index = 0
    # for a in name :
    #     x = ord(a) - ord('A')
    #     y = ord('Z') - ord(a) + 1
    #     if x > y :
    #         x = y
    #     joystick.append(x)
    ## 리스트 컴프리헨션 이용해서 만들수 있음

    while True:
        answer += joystick[index]

        joystick[index] = 0
        
        if sum(joystick) == 0 :
            break

        left, right = 1, 1
        # A가아닌 다른 알파벳이 나올때 까지 좌우로 찾기
        while joystick[index - left] == 0 :
            left += 1
        while joystick[index + right] == 0 :
            right += 1
        
        if left < right :
            answer += left
            index -= left 
        else :
            answer += right
            index += right

        
    # for stick in joystick :
    
    return answer

print(solution("JAZ"))
print(solution("JAN"))
print(solution("JEROEN"))
