def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()

    if str1 == str2: # 둘다 공집합 or 같을 때
        return 65536

    str1 = [str1[i - 1 : i + 1] for i in range(1,len(str1)) if str1[i - 1 : i + 1].isalpha()]
    str2 = [str2[i - 1 : i + 1] for i in range(1,len(str2)) if str2[i - 1 : i + 1].isalpha()]

    section = set(str1) & set(str2) #교집합

    section_sum = sum(min(str1.count(i), str2.count(i)) for i in section) #교집합의 개수 

    answer = int(section_sum / (len(str1) + len(str2) - section_sum) * 65536)

    return answer
    
print(solution('FRANCE', 'french')) 
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
