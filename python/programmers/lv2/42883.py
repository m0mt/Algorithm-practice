def solution(number, k):
    stack = []
    index = 0 

    while k > 0 and index < len(number):
        num = number[index : index + 1]
        if not stack:
            stack.append(num)
            index += 1
        else :
            if stack[-1] < num :
                stack.pop()
                k = k - 1
            else :
                stack.append(num)
                index += 1
    if k > 0:   # number "9999" 식의 문자열 일 때
        return "".join(stack)[0: -k]
    else :
        return "".join(stack) + number[index :]
    

print('1', solution("1924", 2))
print('2', solution("1231234",3))
print('3', solution("4177252841", 4))
print('4', solution("999", 2))








# 첫번째 풀이 # 10번 시간초과
# max_number = max(number[0:len(number) - (num_length - 1)])
# number = number[number.index(max_number) + 1:]
# answer.append(max_number)
# num_length = num_length - 1
# if num_length == len(number):
#     answer += number
#     break

# 두번째 풀이 # 10번 시간초과
# while num_length > 0:
#     end = len(number) - (num_length - 1)
#     max_number = max(number[index:end])
#     index = number.index(max_number, index, end) + 1
#     answer.append(max_number)
#     num_length = num_length -1
#     if num_length == len(number):
#         answer += number
#         break
