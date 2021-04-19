function solution(s) {
    let _s = s;
    let answer = 0;
    const len = _s.length;
    for(let i = 0; i < len; i++) {
        _s = rotaionStr(_s);
        isCorrectStr(_s) && answer++
    }
    return answer;
}

// 올바른 괄호 문자열인지 체크하는 함수
function isCorrectStr(s) {
    // [], {}, () 순으로 개수 체크
    const arr = s.split('');
    const stack = [];
    for(const str of arr) {
        const stackLen = stack.length;
        if (stackLen === 0 || ['[','{','('].includes(str)) {
            stack.push(str);
        } else if (stack[stackLen - 1] === '[' && str === ']') {
            stack.pop();
        } else if (stack[stackLen - 1] === '{' && str === '}') {
            stack.pop();
        } else if (stack[stackLen - 1] === '(' && str === ')') {
            stack.pop();
        } 
    }
    return stack.length === 0 ? true : false;
}

// 문자열 회전 함수
function rotaionStr(s) {
    const arr = s.split('');
    const temp = arr.shift();
    return arr.join('') + temp;
}

console.log(solution('[](){}'));
console.log(solution('}]()[{'));
console.log(solution('[)(]'));
console.log(solution('}}}'));