function solution(n) {
    //solution n의 매개변수를 입력받는다 .
    // n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운 정수를 return 
    const answer  = n.toString().split("").map((i)=>Number(i)).sort((a,b)=>b-a).join("")
    return Number(answer)
    
}
