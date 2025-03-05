'''
# virus
from collections import deque

N = int(input())
Y,X = map(int,input().split())

arr = [[0] * N for _ in range(N)]
q = deque()
q.append((Y,X))
directY = [0,0,1,-1]
directX = [1,-1,0,0]
arr[Y][X] = 1

while q:
    nowy,nowx = q.popleft()
    for i in range(4):
        dy = nowy + directY[i]
        dx = nowx + directX[i]
        if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
            continue
        if arr[dy][dx] != 0:
            continue
        arr[dy][dx] = arr[nowy][nowx] + 1
        q.append((dy,dx))

print(arr[0][0])
'''

'''
# 중간지점 들렸다가 목적지
# 0,0 출발 3,0 들렸다 3,5까지

from collections import deque

arr=[[0,0,0,0,0,0],
     [1,1,0,0,1,0],
     [1,0,0,0,1,0],
     [0,0,0,0,0,0]]

directY = [0,0,1,-1]
directX = [1,-1,0,0]

def bfs(sty,stx,edy,edx):
    q = deque()
    q.append((sty,stx,0))
    used = [[0] * 6 for _ in range(4)]
    used[sty][stx] = 1
    while q:
        y,x,level = q.popleft()
        if y == edy and x == edx:
            return level

        for i in range(4):
            dy = directY[i] + y
            dx = directX[i] + x
            if dy < 0 or dx < 0 or dy > 3 or dx > 5: continue
            if used[dy][dx] == 1: continue
            if arr[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append((dy,dx,level+1))

answer = 0
answer += bfs(0,0,3,0)
answer += bfs(3,0,3,5)
print(answer)
'''

'''
# 섬 사이즈 구하기
from collections import deque

arr = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
]

def bfs(y,x):

    q = deque()
    q.append((y,x))
    used = [[0] * 5 for _ in range(5)]
    used[y][x] = 1
    cnt = 1
    directx = [0,0,1,-1]
    directy = [1,-1,0,0]

    while q:
        nowy,nowx = q.popleft()
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy < 0 or dy > 4 or dx < 0 or dx > 4:
                continue
            if arr[dy][dx] == 0:
                continue
            if arr[dy][dx] == 1 and used[dy][dx] == 0:
                used[dy][dx] = 1
                cnt += 1
                q.append((dy,dx))
    return cnt

for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            tmp = bfs(i,j)

print(tmp)
'''

# 가장 큰 섬 사이즈, 작은 섬 사이즈, 섬의 개수까지
from collections import deque

arr = [
    [0,0,1,0,0,1],
    [0,0,1,0,0,1],
    [0,1,1,1,0,0],
    [0,0,1,0,0,0],
    [1,0,0,0,1,0],
]
used = [[0] * 6 for _ in range(5)]

def bfs(y,x):

    q = deque()
    q.append((y,x))
    size = 1
    directy = [0,0,1,-1]
    directx = [1,-1,0,0]
    used[y][x] = 1

    while q:
        ny,nx = q.popleft()
        for i in range(4):
            dy = ny + directy[i]
            dx = nx + directx[i]
            if dy < 0 or dy > 4 or dx < 0 or dx > 5: continue
            if arr[dy][dx] == 0: continue
            if arr[dy][dx] == 1 and used[dy][dx] == 0:
                used[dy][dx] = 1
                size += 1
                q.append((dy,dx))
    return size

ans = []

for i in range(5):
    for j in range(6):
        if arr[i][j] == 1 and used[i][j] == 0:
            tmp = bfs(i,j)
            ans.append(tmp)

print(f"Max={max(ans)}")
print(f"Min={min(ans)}")
print(f"cnt={len(ans)}")