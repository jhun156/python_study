# import sys
# sys.stdin = open("input.txt","r")

T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [0] * (N+1)
    lst = [list(input().split()) for _ in range(N)]
    for i in range(N):
        arr[int(lst[i][0])] = lst[i][1]

    path = []

    def dfs(level):

        if level > len(arr) - 1:
            return

        dfs(level*2)
        path.append(arr[level])
        dfs(level*2+1)

    dfs(1)
    print(f"#{tc}",end=' ')
    for i in range(N):
        print(path[i],end='')
    print()