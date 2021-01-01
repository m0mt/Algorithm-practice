function solution1(number, k) {
    const result = [];
    const numbers = number.split('');
    let number_len = number.length;
    let index = 0;
    let result_len = 0;
    while(k > 0 && index < number_len) {
        result_len = result.length;
        if (result_len === 0) { 
            result.push(numbers[index]);
            index += 1;
            continue;
        }

        if (result[result_len - 1] >= number[index]) {
            result.push(number[index]);
            index += 1;
        } else {
            result.pop();
            k -= 1;
        }
    }
    answer = '';
    result_len = result.length;
    if (k > 0) { answer += result.slice(0, result_len - k).join(''); }
    if (index < number_len) { answer += result.join('') + numbers.slice(index, number_len).join('') };
    return answer;
}


// 다른 사람 풀이 
// 출처 : https://taesung1993.tistory.com/46
function solution(number, k) {
    const stack = [];
    let answer = '';
    
    for(let i = 0; i < number.length; i++) {
        const el = number[i];

        while(k > 0 && stack[stack.length - 1] < el) {
            stack.pop();
            k -= 1;
            // stack 안에 있는 값이 더 작을경우 계속 해서 비교해서 빼준다.
        }
        stack.push(el);
    }
    // k가 0 일때는 스택 값 자체를 문자열로 만들면 되고,
    // k > 0 일때 stack의 k번째 값만 없애주고 문자열로 만든다.
    stack.splice(stack.length - k, k);
    answer = stack.join('');
    return answer;
}


console.log(solution('1924', 2));
console.log(solution('1231234', 3));
console.log(solution('4177252841', 4));
console.log(solution('987654321', 8))