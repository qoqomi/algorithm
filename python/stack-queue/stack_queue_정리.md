## input()
- 파이썬 내장 함수 
- 사용자가 입력한 "한줄"을 문자열(str)로 변환한다. 

---
# 📌 문자열 뒤집기

## 1. list() + reverse()

### 예시
```python
a = 'abcde'
b = list(a)
b.reverse()
c = ''.join(b) #edcba
```

### ❌ 틀린 사용
👉 reverse()는 리턴값이 없고, 자기 자신을 변경함
```python
list(a).reverse() # None 내부만 바뀜
```
### ✅ 올바른 흐름
```python
b = list(a)
b.reverse()
```

## 2. reversed() 함수
```python
a = 'abcde'
b = reversed(a) 
c = ''.join(b)
```
👉 reversed()는 뒤집힌 "결과"가 아니라 "iterator" 반환

> iterator: 하나씩 커내서 사용할 수 있는 객체

## 3. 슬라이싱[::-1](제일 많이 씀)
```python
a = 'abcde'
b = a[::-1] # edcba
```
### [::-1] 의미 
[start : end : step]
👉 의미
- start: 처음부터
- end: 끝까지
- step: -1 (뒤로 가기)

---

# 최빈값 구하기

## 1. 배열 인덱싱 매핑 
```python
index = ord(char) - ord('a')
```
문자를 숫자로 변환하는 것

a~z:몇개가 나왔는지 저장해야함 
배열은 값을 어떻게 저장? Index에 저장 

ord("a") -> 97번 
ord("a") - 97 = 0
[0]번째 숫자가 됨

chr() ->문자로 변경하는 역 연산 