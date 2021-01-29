// 첫번째 풀이
function solution(dartResult) {
    const bonus = ['S','D','T'];
    const options = ['*', '#'];
    let answer = [];
    let result = '';
    for (let dart of dartResult) {
        if(bonus.includes(dart)) {
            result = Number(result);
            switch(dart) {
                case bonus[0]:
                    result = Math.pow(result, 1);
                    break;
                case bonus[1]:
                    result = Math.pow(result, 2);
                    break;
                case bonus[2]:
                    result = Math.pow(result, 3);
                    break;
            }
            answer.push(result);
            result = '';
        } else if(options.includes(dart)) {
            switch(dart) {
                case options[0]:
                    for (let i = answer.length - 2 < 0 ? 0 : answer.length - 2; i < answer.length; i++) {
                        answer[i] *= 2;
                    }
                    break;
                case options[1]:
                    answer[answer.length - 1] *= (-1);
                    break;
            }
        } else {
            result += dart
        }
    }
    return answer.reduce((a, b) => a + b);
}
// S, D, T 점수 1제곱, 2제곱, 3제곱
// * 스타상 -> 해당 점수와 바로전에 얻은 점수를 각2배
// # 아차상 -> 해당 점수는 마이너스
// 스타상 첫번째 기회에 나올 시 첫번째 스타상의 점수만 2배
// 스타상 중첩 가능, 아차상 -> -2배로 된다.
// S, D, T 점수마다 하나씩 존재
// *, # 점수마다 둘 중 하나만 존재 or 존재 x

console.log(solution('1S2D*3T'));
console.log(solution('1D2S#10S'));
console.log(solution('1D2S0T'));
console.log(solution('1S*2T*3S'));
console.log(solution('1D#2S*3S'));
console.log(solution('1T2D3D#'));
console.log(solution('1D2S3T*'));
