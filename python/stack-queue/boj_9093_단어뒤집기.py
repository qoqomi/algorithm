n = int(input())

for i in range(n):
    reverse = []
    words = input().split()
    for chunk in words:
        reverse.append(chunk[::-1])

    print(" ".join(reverse))
