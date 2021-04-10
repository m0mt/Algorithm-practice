function solution1(dirs) {
    let answer = 0;
    const location = {x: 0, y: 0};
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    const direction = ['U', 'D', 'L', 'R'];
    const visited = [];

    for (const dir of dirs) {
        const prev = [location.x, location.y];
        const index = direction.indexOf(dir);
        location.x += dx[index];
        location.y += dy[index];
        if (location.x < -5 || location.x > 5 || location.y < -5 || location.y > 5) {
            [location.x, location.y] = prev;
            continue;
        }
        // 방문한 기록이 있을 때의 처리만 하면 된다.
        if (!visited.includes([prev[0], prev[1], location.x, location.y].join(''))) {
            visited.push([prev[0], prev[1], location.x, location.y].join(''));
            visited.push([location.x, location.y, prev[0], prev[1]].join(''));
            answer += 1;
        }
    }
    return answer;
}


// 다른 사람 풀이
// 풀이 방식은 비슷 하지만 map과 set을 사용하는 점을 잘 활용 할 것
// 각 기능 마다 함수로 나눌 수 있도록 코딩을 할 것
function solution(dirs) {
    const firstPathMap = new Map();
    let now = [0, 0];
    let moved;
    for(let dir of dirs) {
        moved = move(now, dir);
        if(moved[0] < -5 || moved[0] > 5 || moved[1] < -5 || moved[1] > 5) {
            continue;
        }
        firstPathMap.set(generateKey(now, moved), true);
        now = moved;
    }  
    return firstPathMap.size;
}

function move(now, dir) {
    switch(dir) {
        case 'L': 
            return [now[0] - 1, now[1]];
        case 'R':
            return [now[0] + 1, now[1]];
        case 'U':
            return [now[0], now[1] + 1];
        case 'D':
            return [now[0], now[1] - 1];
    }        
}

function generateKey(now, moved) {
    return `${Math.min(now[0], moved[0])},${Math.max(now[0], moved[0])},${Math.min(now[1], moved[1])},${Math.max(now[1], moved[1])}`;
}
console.log(solution("ULURRDLLU"));
console.log(solution("LULLLLLLU"));