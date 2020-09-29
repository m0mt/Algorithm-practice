def solution(phone_number):
    length = len(phone_number) - 4
    answer = ''
    for _ in range(length):
        answer += '*'
    answer += phone_number[-4 :]


    return answer

