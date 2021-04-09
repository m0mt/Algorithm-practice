// 다른 사람의 풀이
// dfs (너비 우선 탐색) 은 stack을 사용
// bfs (깊이 우선 탐색) 은 queue를 사용
function solution(maps) {
    let answer = -1;
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    const n = maps.length;
    const m = maps[0].length;
    const visited = Array.from(Array(n), () => Array(m).fill(false));
    const queue = [[0, 0, 1]];
    let queueLength = queue.length;

    while (queueLength !== 0) {
        const [x, y, distance] = queue.shift();
        for(let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];
            if(nx < 0 || ny < 0 || nx > n - 1 || ny > m - 1 || maps[nx][ny] === 0 || visited[nx][ny]) continue;
            visited[nx][ny] = true;
            queue.push([nx, ny, distance + 1]);
        }
        if (x === n - 1 && y === m - 1) {
            answer = distance;
            break;
        }
        queueLength = queue.length;
    }
    return answer
}


// 내 다른 풀이 
// 각 지점마다 갈 수있는 최솟값을 구해서 
// 마지막 도착 지점이 변하지 않았다면 -1 아니면 최솟값을 출력하도록 하는 방법
// 런타임 에러, 7, 11, 13 오류
function solution1(maps) {
    const n = maps.length;
    const m = maps[0].length;
    function findMinDistance(x, y, maps, distance) {
        if(x < 0 || x > n - 1 || y < 0 || y > m - 1 || maps[x][y] === 0 || (maps[x][y] !== 1 & maps[x][y] <= distance)) {
            return false;
        }
        maps[x][y] = distance + 1;
        console.log(maps);
        const dx = [0, 0, 1, -1];
        const dy = [1, -1, 0, 0];
    
        for (let i = 0; i < 4; i++) {
            findMinDistance(x + dx[i], y + dy[i], maps, maps[x][y]);
        }
    }
    findMinDistance(0, 0, maps, distance);
    return maps[n - 1][m - 1] === 1 ? -1 : maps[n - 1][m - 1]; 
}

console.log(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])); // 11
console.log(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])); // -1

// const arr1 = Array.from(Array(5), () => Array(2).fill(false));
// console.log(arr1);