// 개발 언어 cpp, java, python 중 하나
// 지원 직군 back, front 중 하나
// 지원 경력 junior, senior 중 하나
// 소울푸드 chicken, pizza 중 하나
// 조건에 따라서 count 하시오.
function solution( info, query ) {
    const answer = [];
    const infoMap = makeDatabase(info);
    
    for (const key in infoMap) {
        infoMap[key] = infoMap[key].sort((a, b) => a - b);
    }
    for (const q of query) {
        answer.push(findCandidate(infoMap, q));
    }
    return answer
}

function makeDatabase( info ) {
    const infoMap = {};

    for (const i of info) {
        const splited = i.split(' ');
        const score = Number(splited.pop());
        makeCombinationData(splited, score, 0);
    }
    
    function makeCombinationData( infoArr, score, start ) {
        const key = infoArr.join('');
        infoMap[key] ? infoMap[key].push(score) : infoMap[key] = [score];
        for (let i = start; i < infoArr.length; i++) {
            const temp = [...infoArr];
            temp[i] = '-';
            makeCombinationData(temp, score, i + 1)            
        }
    }
    return infoMap
}

function findCandidate( infoMap, querys ) {
    const splitedQuery = querys.replace(/and\s/gi, '').split(' ');
    const score = Number(splitedQuery.pop());
    const key = splitedQuery.join('');
    let value = 0;
    if (infoMap[key]) {
        let start = 0;
        // length - 1 이 아닌 이유는 배열의 값이 1개 일 경우 반복문이 돌지 않고 값이 측정 되기 때문
        let end = infoMap[key].length;
        while (start < end) {
            const mid = Math.floor((start + end) / 2);
            if (infoMap[key][mid] < score) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        value = infoMap[key].length - start;
    } else {
        value = 0;
    }
    return value
}

console.log(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
// [ 1, 1, 1, 1, 2, 4]