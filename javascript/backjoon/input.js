// 한칸 띄어쓰기로 구분
let input = require('fs')
    .readFileSync('/dev/stdin')
    .toString()
    .split(' ');

// 줄바꿈으로 구분
let input = require('fs')
    .readFileSync('/dev/stdin')
    .toString()
    .split('\n');

// 숫자일 때 
let input = require('fs')
    .readFileSync('/dev/stdin')
    .toString()
    .split(' ')
    .map((a) => +a);

