function solution(d, budget) {
    let answer = 0;
    let _d = d.sort((a, b) => b - a);
    let i = 0;
    let cnt = 0;

    while (i <= budget) {
        i += _d.pop();
        cnt += 1;
    }
    return cnt - 1;
}

console.log(solution([1,3,2,5,4],9));
console.log(solution([2,2,3,3],10));