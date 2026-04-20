from re import S
import sys

input = sys.stdin.readline

N = int(input())
stack = []
for n in range(N):

    str = input().split()
    order = str[0]

    if order == "push":
        stack.append(str[1])
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    else:
        if order == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif order == "top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
