# 1주차: 시간복잡도 & 공간 복잡도 

## 시간복잡도 판단하기

 > 입력값에 비해 얼마나 일을 수행해야 하는가? 

1) 각 줄이 실행되는 걸 1번의 연산이 된다고 생각하기
2) N과 N^2은 N이 커질수록 더 큰 차이가 남 
3) N의 지수를 먼저 비교하기 
4) for문과의 연산은 곱, 이외의 값은 덧셈


## 공간복잡도 판단하기 

## 점근 표기법 
> 어떤 함수의 증가 양상을 다른 함수와 비교로 표현하는 수론과 해석학의 방법이다. 


```python
def is_number_exist(number, array):
    for i in array:
        if number == i:
            return True
    return False
```