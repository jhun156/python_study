# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = [list(map(int,input().strip())) for _ in range(N)]

def dfs(y,x,cnt):

    visited[y][x] = cnt
    dY = [0,0,1,-1]
    dX = [1,-1,0,0]
    for i in range(4):
        dy = y + dY[i]
        dx = x + dX[i]
        if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
            continue
        if arr[dy][dx] == 0:
            continue
        if visited[dy][dx] != 0:
            continue
        visited[dy][dx] = cnt
        dfs(dy,dx,cnt)


visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            dfs(i,j,cnt)

DAT = [0] * 1000
for i in range(N):
    for j in range(N):
        DAT[visited[i][j]] += 1

result = []
for i in range(1,1000):
    if DAT[i] == 0:
        break
    result.append(DAT[i])

result.sort()
print(len(result))
for i in result:
    print(i)