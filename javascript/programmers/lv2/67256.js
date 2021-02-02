function solution(numbers, hand) {
    var answer = '';
    const left = [3, 0];
    const right = [3, 2];
    const key_left = [1, 4, 7];
    const key_middle = [2, 5, 8, 0];
    const key_right = [3, 6, 9];
    
    for (let number of numbers) {
        if (key_left.includes(number)) {
            answer += 'L';
            [left[0], left[1]] = [key_left.indexOf(number) , 0];
        } else if (key_right.includes(number)) {
            answer += 'R';
            [right[0], right[1]] = [key_right.indexOf(number) , 2];
        } else {
            const key_y = key_middle.indexOf(number);
            if((Math.abs(left[0] - key_y) + Math.abs(left[1] - 1)) < (Math.abs(right[0] - key_y) + Math.abs(right[1] - 1))) {
                answer += 'L';
                [left[0], left[1]] = [key_middle.indexOf(number) , 1];
            } else if ((Math.abs(left[0] - key_y) + Math.abs(left[1] - 1)) > (Math.abs(right[0] - key_y) + Math.abs(right[1] - 1))) {
                answer += 'R';
                [right[0], right[1]] = [key_middle.indexOf(number) , 1];
            } else {
                answer += (hand === 'left' ? 'L' : 'R');
                hand === 'left' ? ([left[0], left[1]] = [key_middle.indexOf(number) , 1]) : ([right[0], right[1]] = [key_middle.indexOf(number) , 1]);
            }
        }
    }
    return answer;
}
console.log(solution([1,3,4,5,8,2,1,4,5,9,5], 'right')); // LRLLLRLLRRL
console.log(solution([7,0,8,2,8,3,1,5,7,6,2], 'left')); // LRLLRRLLLRR
console.log(solution([1,2,3,4,5,6,7,8,9,0], 'right')); // LLRLLRLLRL


// 다른사람의 풀이 
// 키패드를 그리드 형식으로 표현해서 풀이
// const grid = [[0,-2], [-1,1], [0,1],
//               [1,1], [-1,0], [0,0],
//               [1,0], [-1,-1], [0,-1],
//               [1,-1], [-1,-2], [1,-2]];