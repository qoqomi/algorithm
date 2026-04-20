import sys

input = sys.stdin.readline

n, k = map(int, input().split())

num_list = list(range(1, n + 1))
index = k - 1
result = []

while num_list:
    result.append(num_list.pop(index))
    index = index + k - 1

    if len(num_list) > 0:
        while index >= len(num_list):
            index = index - len(num_list)

print("<", end="")
print(*result, sep=", ", end="")
print(">", end="")
