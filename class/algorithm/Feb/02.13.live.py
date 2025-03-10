'''
def push(item,size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item

top = -1
stack = [0] * 10

top += 1
stack[top] = 1

top += 1
stack[top] = 2

top += 1
stack[top] = 3

top -= 1
print(stack[top+1])
top -= 1
print(stack[top+1])
print(stack[top])
top -= 1
'''
'''
txt = input()

top = -1
stack = [0] * 100

ans = 1     # 짝이 맞다고 가정
for x in txt:
    if x == '(':    # 여는 괄호 push
        top += 1
        stack[top] = x
    elif x == ')':  # 닫는 괄호
        if top == -1:
            ans = 0
            break
        else:
            top -= 1

if top > -1:
    ans = 0
print(ans)
# 1218 괄호 짝짓기 참고
'''

def f(i,N):
    if i == N:
        return
    else:
        print(arr[i])
        f(i+1,N)








