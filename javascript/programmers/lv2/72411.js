function solution(orders, course) {
    var answer = [];
    for(const num of course) {
        const courseData = {};
        for (const order of orders) {
            const orderArray = order.split('');
            for (const item of getCombinations(orderArray, num)) {
                const key = item.sort().join('');
                courseData[key] = courseData[key] ? courseData[key] + 1 : 1;
            }
        }
        const maxValue = Math.max(...Object.values(courseData));
        for(let course of Object.entries(courseData)) {
            course[1] === maxValue && course[1] >= 2 && answer.push(course[0])
        }
    }
    function getCombinations(arr, selectNumber) {
        const results = [];
        if (selectNumber === 1) return arr.map((value) => [value]);
      
        arr.forEach((fixed, index, origin) => {
          const rest = origin.slice(index + 1);
          const combinations = getCombinations(rest, selectNumber - 1);
          const attached = combinations.map((combination) => [fixed, ...combination]);
          results.push(...attached);
        });

        return results
    }

    return coursemenuSort(answer);
}

function coursemenuSort(array) {
    // localeCompare()
    return array.sort();
}

console.log(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]));
console.log(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]));
console.log(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]));