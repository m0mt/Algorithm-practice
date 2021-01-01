function solution(numbers) {
    let answer = new Set();
    
    for(let i = 0 ; i < numbers.length; i++){        
      for(let j = i + 1; j < numbers.length; j++){
        answer.add(numbers[i] + numbers[j]);
      }
    }
    
    let _answer = [...answer].sort((a,b)=> a-b);
    answer = _answer
    
    return answer;
}
console.log(solution([2,1,3,4,1]))
console.log(solution([5,0,2,7]))