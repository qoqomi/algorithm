function solution(sizes) {
    // 1. sizes안에 숫자 몰아주기 0이 크면 0,1 아니면 1,0 으로 큰 수와 작은 수를 한 쪽으로 몬다. 
    let arr = sizes.map((size)=>size [0] > size[1] ? [size[0], size[1]]: [size[1],size[0]])
    
    let width = [];
    let height = [];
    
    for(let i = 0; i < arr.length; i++){
            width.push(arr[i][0])
            height.push(arr[i][1])
    }
    return Math.max(...width) * Math.max(...height)
}