input = 20

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]`


def find_prime_list_under_number_2(number):
    arr = []
    # arr : 1과 자신 외에 아무것도 나눌 수 없음
    # N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
    for n in range(2, number + 1):
        # 모든 소수들과 비교
        for i in arr:
            if i * i <= n and n % i == 0:
                break
        else:
            arr.append(n)

    return arr


# 결과: 짝수 없음 (리스트에 짝수가 없으니까)


result = find_prime_list_under_number_2(input)
print(result)

## [2, 3, 5, 7, 11, 13, 17, 19]
