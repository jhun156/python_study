# 1. 숫자나오면 result에 그냥 추가
# 2. 연산자의 경우
# 스택이 비어있으면 그냥 push
# new > 기존 그냥 push
# new <= 기존 pop.push
# 3. 스택에 남은 것들 result에 추가

# 3+4*5+6*2

# 계산
# 숫자나오면 stack에 push
# 연산자 pop 2개 이후 연산자 적용해서 stack에 push
# 마지막 남은 값이 정답

# import sys
# sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = input()
    stack = []
    result = ''
    priority = {'+': 1, '*': 2}
    for i in arr:
        if i.isdigit():
            result += i
        else:
            if stack and priority[i] <= priority[stack[-1]]:
                result += stack.pop()
            stack.append(i)
    while stack:
        result += stack.pop()

# 계산
    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(a + b)
            else:
                stack.append(a * b)

    ans = stack.pop()
    print(f"#{tc} {ans}")
