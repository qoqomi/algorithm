def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for i in array:
        if number == i:
            return True
    # for문 돌때까지 true가 아니므로 false 반환
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3, 5, 6, 1, 2, 4]))
print("정답 = False 현재 풀이 값 =", result(7, [6, 6, 6]))
print("정답 = True 현재 풀이 값 =", result(2, [6, 9, 2, 7, 1888]))
