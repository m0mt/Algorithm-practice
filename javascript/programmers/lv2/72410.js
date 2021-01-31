// 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
// 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
// 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
// 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
// 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
// 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
//      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
// 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


function removeString(new_id) {
    const result = [];
    // isNan(), ['-','_','.'] 등으로 대체가능
    const exception = /[a-z0-9.\-_]/;
    for (let i of new_id) {
        if (exception.test(i)){
            result.push(i);
        }
    }
    return result.join('');
}

function checkContinousFullstop(new_id) {
    const result = [];
    let index = -1;
    for (let i of new_id) {
        if (i === '.' && result[index] === '.') {
            continue;
        } else {
            index += 1
            result.push(i);
        }
    }
    return result.join('');
}

function checkStartEndFullstop(new_id) {
    const length = new_id.length;
    let start = 0;
    let last = length;
    if(new_id.charAt(0) === '.') { start = 1 }
    if(new_id.charAt(length - 1) === '.') { last = length - 1 }
    // new_id.substring(start, last)
    return new_id.slice(start, last);
}

function checkEmptyString(new_id) {
    if (new_id === '') { new_id = 'aaa'; }
    return new_id
}

function checkLengthOver15(new_id) {
    return new_id.slice(0, 15);
}

function checkLengthUnder2(new_id) {
    const length = new_id.length;
    if (length < 3) {
        for(let i = length; i < 3; i++) {
            new_id += new_id[length - 1];
        }
    }
    return new_id
}

function solution(new_id) {
    new_id = new_id.toLowerCase();
    new_id = removeString(new_id);
    new_id = checkContinousFullstop(new_id);
    new_id = checkStartEndFullstop(new_id);
    new_id = checkEmptyString(new_id);
    new_id = checkLengthOver15(new_id);
    new_id = checkStartEndFullstop(new_id);
    new_id = checkLengthUnder2(new_id);
    return new_id;
}



console.log(solution("...!@BaT#*..y.abcdefghijklm"));
console.log(solution("z-+.^."));
console.log(solution("=.="));
console.log(solution("123_.def"));
console.log(solution("abcdefghijklmn.p"));

// 정규표현식을 이용한 다른사람의 풀이
function solutoin(new_id) {
    const answer = new_id
        .toLowerCase() // 1번째 조건
        .replace(/[^\w-_.]/g, '') // 2번째 조건
        .replace(/\.+/g, '.') // 3번째 조건
        .replace(/^|.|\.$/g, '') // 4번째 조건
        .replace(/^$/, 'a') // 5번째 조건
        .slice(0, 15).replace(/\.$/, ''); // 6번째 조건
    const len = answer.length;
    return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
}