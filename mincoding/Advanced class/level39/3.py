N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def dfs(level,start):

    global ans
    if level > ans:
        ans = level

    for i in range(N):
        if arr[i][0] >= start and used[i] == 0:
            used[i] = 1
            dfs(level+1,arr[i][1])
            used[i] = 0


ans = 0
used = [0] * N
dfs(0,1)
print(ans)