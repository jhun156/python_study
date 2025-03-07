# import sys
# sys.stdin = open("input.txt","r")

def inorder(now):

    global value
    if now > N:
        return
    inorder(now*2)
    tree[now] = value
    value += 1
    inorder(now*2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    value = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N // 2]}')