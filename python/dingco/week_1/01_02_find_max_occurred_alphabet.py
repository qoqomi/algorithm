def find_max_occurred_alphabet(string):
    array = [0] * 26

    for i in string:
        if i.isalpha():
            num = ord(i) - ord("a")
            array[num] += 1

    return array


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
