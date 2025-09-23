function solution(n, l, r) {
    if(n === 0) return 1;
    
    
    let answer = 0;
    for(let i =l-1;i<r; i++){
        if(!i.toString(5).match(2)){
            answer ++;
        }
        
    }
    console.log(answer)
    return answer
    
}