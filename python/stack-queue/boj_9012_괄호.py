n = input()


for _ in range(int(n)):
    str = input()  # (())())
    stack = []
    for s in str:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack) == 0:
                break
            else:
                stack.pop()

if len(stack) == 0:
    print("YES")
else:
    print("NO")
