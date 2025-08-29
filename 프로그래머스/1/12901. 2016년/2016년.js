function solution(a, b) {
    // 윤년 : 2월 29일 존재 , 366일 
    // 4,100,400으로 나눠지는 년도 
    const weekDay = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    const lastMonth = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    let day = b + 4
    
    for(let i =0; i < a-1; ++i){
        
        day+= lastMonth[i]
    }
     
    return weekDay[day%7]
}