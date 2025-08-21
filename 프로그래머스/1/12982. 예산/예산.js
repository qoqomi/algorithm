function solution(d, budget) {
    const result = d.sort((a,b)=>a-b)
    let count = 0
    for(let i = 0; i < d.length; i++){
        if(d[i] > budget) {
            break;
        }
        console.log("result",count)
        budget -= d[i]
        count += 1
    }
  
    return count
}