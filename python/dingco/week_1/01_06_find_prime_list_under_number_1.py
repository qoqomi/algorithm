input = 20

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]`


def find_prime_list_under_number(number):
    # 소수: 나자신과 1 외 아무것도 나눌 수 없음
    result = []

    for i in range(2, number + 1):
        print(result)
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            result.append(i)
    return result


result = find_prime_list_under_number(input)
print(result)

## [2, 3, 5, 7, 11, 13, 17, 19]
