# import sys
# sys.stdin = open("input.txt","r")

arr = [list(input()) for _ in range(4)]
N = int(input())
ans = []
path = [0] * N
visited = [[0] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        if arr[i][j] == '_':
            visited[i][j] = '_'

dY = [0,0,1,-1]
dX = [1,-1,0,0]
Max = -1

def bomb(y,x):

    for i in range(4):
        dy = y + dY[i]
        dx = x + dX[i]
        if dy < 0 or dy > 3 or dx < 0 or dx > 3:    continue
        if visited[dy][dx] == '_':  continue
        visited[dy][dx] += 1

def clean(y,x):

    for i in range(4):
        dy = y + dY[i]
        dx = x + dX[i]
        if dy < 0 or dy > 3 or dx < 0 or dx > 3:    continue
        if visited[dy][dx] == 0:    continue
        if visited[dy][dx] == '_':  continue
        visited[dy][dx] -= 1

def dfs(level):

    global Max, ans
    if level == N:
        cnt = 0
        for i in range(4):
            for j in range(4):
                if visited[i][j] != '_' and visited[i][j] > 0:
                    cnt += 1
        if Max < cnt:
            Max = cnt
            ans = path[:]
            return
        return

    for i in range(4):
        for j in range(4):
            if visited[i][j] == 0 and arr[i][j] != '_':
                visited[i][j] = 1
                path[level] = arr[i][j]
                bomb(i,j)
                dfs(level+1)
                visited[i][j] = 0
                clean(i,j)

dfs(0)
ans.sort()
print(*ans)