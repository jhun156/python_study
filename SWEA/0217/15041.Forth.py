# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    stack = []
    lst = list(input().split())
    try:
        for i in lst:
            if i.isdigit():
                stack.append(int(i))
            elif i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b//a)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
        if len(stack) != 1:
            print(f"#{tc} error")
        else:
            ans = stack.pop()
            print(f"#{tc} {ans}")
    except Exception as e:
        print(f"#{tc} error")
