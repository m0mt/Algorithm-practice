from itertools import permutations
def solution(expression):
    answer = 0
    e = list(permutations(('+','-','*')))

    def calc(equation, n, expression):
        if n == 2 :
            return str(eval(expression))
        if equation[n] == '+':
            result = eval("+".join(calc(equation, n + 1, ex) for ex in expression.split('+')))            
        if equation[n] == '*':
            result = eval("*".join(calc(equation, n + 1, ex) for ex in expression.split('*')))            
        if equation[n] == '-':
            result = eval("-".join(calc(equation, n + 1, ex) for ex in expression.split('-')))            
        return str(result)

    for equation in e:
        res = int(calc(equation, 0, expression))
        answer = max(abs(res), answer)

    return answer


print(solution("100-200*300-500+20")) # 60420
print(solution("50*6-3*2")) # 300