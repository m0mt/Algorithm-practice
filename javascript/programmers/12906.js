function solution(arr) {
    let answer = [];
    let key = -1;
    
    for(let i = 0; i < arr.length; i++){
        if(key !== arr[i]){
            key = arr[i];
            answer.push(key);
        }
    }
    return answer;
};

function solution1(arr) {
    let answer = [];
    for(let i of arr) {
        num = answer.slice(-1)[0];
        if(num !== i){
            answer.push(i);
        }
    }
    return answer
};
// 예전 코드

console.log(solution([1,1,3,3,0,1,1]));
console.log(solution([4,4,4,3,3]));