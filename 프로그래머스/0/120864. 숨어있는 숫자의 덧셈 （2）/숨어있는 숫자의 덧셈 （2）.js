function solution(my_string) {
    // "\d": 숫자 하나 (0~9)
    // /g : global
    // 
     const numbers = my_string.match(/\d+/g)
     if(!numbers) return 0;
    
    return numbers.reduce((sum,num)=>sum + Number(num),0);
}