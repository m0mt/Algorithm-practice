function solution(n, arr1, arr2) {
    let answer = [];
    for (let i = 0; i < n; i++) {
        let result = '';
        const number1 = lpad(arr1[i].toString(2), n).split('');
        const number2 = lpad(arr2[i].toString(2), n).split('');
        for (let j = 0; j < n; j++) {
            if (number1[j] === '1' || number2[j] === '1') {
                result += '#';
            } else {
                result += ' ';
            }
        }
        answer.push(result);
    }
    return answer;
}

function lpad(str, n) {
    const str_length = str.length;
    if (str_length >= n) {
        return str
    }

    let pad_str = '';
    for (let i = 0; i < n - str_length; i++) {
        pad_str += '0';
    }
    return pad_str + str
}

console.log(solution1(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution1(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]));

// 다른사람의 풀이 
// /1|0/g 의 정규표현식을 이용
function solution1(n, arr1, arr2) {
    return arr1.map((v, i) => addZero(n, (v | arr2[i]).toString(2)).replace(/1|0/g, a => +a ? '#' : ' '));
}

function addZero(n, s) {
    return '0'.repeat(n - s.length) + s;
}