import sys
sys.stdin = open("input.txt","r")
from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]
sty,stx = map(int,input().split())
edy,edx = 0,0

water = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '$':
            edy,edx = i,j
        elif arr[i][j] == 'A':
            water.append([i,j])

def bfs1(sy,sx,ey,ex,level):
    q = deque()
    q.append((sy,sx,level))
    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] = 1
    directy = [0,0,1,-1]
    directx = [1,-1,0,0]
    Min = 21e8

    while q:
        ny,nx,level = q.popleft()
        for i in range(4):
            dy = ny + directy[i]
            dx = nx + directx[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
                continue
            if visited[dy][dx] == 1:
                continue
            if arr[dy][dx] == '$' or arr[dy][dx] == '#':
                continue
            if visited[dy][dx] == 0:
                visited[dy][dx] = 1
                q.append((dy,dx,level+1))
                if dy == ey and dx == ex:
                    if Min > level+1:
                        Min = level + 1
    return Min


def bfs2(sy, sx, ey, ex, level):
    q = deque()
    q.append((sy, sx, level))
    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] = 1
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    Min = 21e8

    while q:
        ny, nx, level = q.popleft()
        for i in range(4):
            dy = ny + directy[i]
            dx = nx + directx[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
                continue
            if visited[dy][dx] == 1:
                continue
            if arr[dy][dx] == '#':
                continue
            if visited[dy][dx] == 0:
                visited[dy][dx] = 1
                q.append((dy, dx, level+1))
                if dy == ey and dx == ex:
                    if Min > level + 1:
                        Min = level + 1
    return Min

ans = []

for i in range(len(water)):
    tmp = 0
    midy,midx = water[i][0],water[i][1]
    tmp += bfs1(sty,stx,midy,midx,0)
    tmp += bfs2(midy,midx,edy,edx,0)
    ans.append(tmp)

print(min(ans))
