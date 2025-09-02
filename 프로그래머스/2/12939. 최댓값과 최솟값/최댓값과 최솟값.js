function solution(s) {
    const arr = s.split(" ").map((item)=>Number(item))
    let min = Math.min(...arr)
    let max = Math.max(...arr)
    
    return `${min} ${max}`
}