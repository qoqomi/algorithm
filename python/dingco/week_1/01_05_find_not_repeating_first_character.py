input = "abadabac"


def find_alphabet_occurrence_array(string):
    array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord("a")
        array[index] += 1
    return array


def find_not_repeating_first_character(string):
    # O(N)
    occurrence_array = find_alphabet_occurrence_array(string)
    not_repeating_character_array = []

    for i in range(len(occurrence_array)):
        # 0(26) -> 1이다 항상 26번 반복함
        if occurrence_array[i] == 1:
            not_repeating_character_array.append(chr(i + ord("a")))
    print("📌", not_repeating_character_array)
    for char in string:
        if char in not_repeating_character_array:
            return char

    print(find_alphabet_occurrence_array(string))
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
