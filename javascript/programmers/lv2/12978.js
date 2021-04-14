// 문제 풀이
// road 배열 중에서 값이 두번 나올 경우도 있다고 해서
// road 배열을 index 2번의 값을 기준으로 내림차순으로 정렬 한뒤 값을 넣으면 정리 된다.
function solution(N, road, K) {
    let answer = 0;
    const _road = sortRoad(road);
    const graph = makeGraph(N, _road);
    for(const distance of graph[0]) {
        distance <= K && (answer += 1);
    }    
    return answer;
}

const makeGraph = (N, road) => {
    const INF = 10000000;
    const graph = Array.from(Array(N), () => Array(N).fill(INF));

    for(let info of road) {
        const [x, y, distance] = info;
        graph[x - 1][y - 1] = distance;
        graph[y - 1][x - 1] = distance;
    }
    
    for(let i = 0; i < N; i++) {
        graph[i][i] = 0;
    }
    return floydWarshall(graph);
}   

const sortRoad = (road) => {
    const _road = road.sort((a, b) => b[2] - a[2])
    return _road
}

const floydWarshall = (graph) => {
    const len = graph.length;
    const _graph = [...graph];
    for (let k = 0; k < len; k++) {
        for(let i = 0; i < len; i++) {
            for (let j = 0; j < len; j++) {
                const value = _graph[i][k] + _graph[k][j];
                if (value < _graph[i][j]) {
                    _graph[i][j] = value;
                }
            }
        }
    }
    return _graph
}

console.log(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)); // 4
console.log(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)); // 4 