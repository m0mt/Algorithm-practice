function solution(s) {
    let length = s.length;
    let idx = Math.floor(length / 2);
    let answer = length % 2 === 0 ? s.substr(idx - 1 , 2) : s.substr(idx, 1);
    return answer;
}