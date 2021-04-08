// 다른 사람의 풀이
function solution(maps) {
    let dx = [0,0,1,-1];
    let dy = [1,-1,0,0];    
    var answer = -1;
    const q = [[0,0,1]];

    while(q.length!=0){
        let y = q[0][0];
        let x = q[0][1];
        let cnt = q[0][2];
        q.shift();
        if(y === maps.length-1 && x === maps[0].length - 1){
            answer = cnt;
            break;
        }
        for(let i=0;i<4;i+=1){
            let ny = y+dy[i];
            let nx = x+dx[i];
            if(nx < 0 || ny < 0 || nx >= [0].length || ny >= maps.length)continue;
            if(maps[ny][nx] == 2)continue;//방문했을 때
            if(maps[ny][nx] == 0)continue; //벽일 때
            maps[ny][nx] = 2;
            q.push([ny, nx, cnt + 1]);  
        }
    }
    return answer;
}

// function solution(maps) {
//     let answer = 0;
//     const n = maps.length;
//     const m = maps[0].length;
//     const visited = Array.from(Array(n), () => Array(m).fill(false));
//     findRoad(0, 0, maps, visited, answer);
//     return answer;
// }

// function findRoad(x, y, maps, visited, answer) {
//     if(x < 0 || x > 4 || y < 0 || y > 4 || maps[x][y] === 0 || visited[x][y] === true) {
//         return false;
//     }
    
//     visited[x][y] = true;
//     answer += 1;
//     console.log(answer);
//     findRoad(x + 1, y, maps, visited, answer)
//     findRoad(x - 1, y, maps, visited, answer)
//     findRoad(x, y + 1, maps, visited, answer)
//     findRoad(x, y - 1, maps, visited, answer)
// }

// console.log(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])); // 11
// // console.log(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])); // -1

// // const arr1 = Array.from(Array(5), () => Array(2).fill(false));
// // console.log(arr1);