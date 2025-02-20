# import sys
# sys.stdin = open("input.txt","r")

T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = input()
    # (1) 중위표기식을 후위표기식으로 변경
    # 1. result라는 변수에 숫자는 그냥 저장
    # 2. 연산자라면 스택이 비어있으면 그냥 넣고, 아니면 pop 한걸 result에 푸시하고 push
    # 3. 마지막으로 스택에 남은 연산자들은 모두 result로 옮기기

    stack = []
    result = ''
    for i in arr:
        if i == '+':
            if not stack:                   # 비어있다면 push
                stack.append(i)
            else:
                result += stack.pop()       # 비어있지않다면
                stack.append(i)
        elif i.isdigit():
            result += i
    result += stack.pop()           # result가 결과 후위표기법식

    # (2) 후위표기식을 계산해서 출력하기
    # 1. 숫자는 그냥 stack에 push
    # 2. 연산자는 stack에서 2개 pop 한다음 연산하고 넣기
    # 3. 마지막에 남아있는게 정답

    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
    ans = stack.pop()

    print(f"#{tc} {ans}")