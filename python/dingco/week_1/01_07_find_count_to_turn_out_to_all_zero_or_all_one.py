input = "011110"

string = input()


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    zero = list(filter(None, string.split("0")))
    one = list(filter(None, string.split("1")))

    return min(len(zero), len(one))


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
