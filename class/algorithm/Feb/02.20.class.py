'''
# BFS tree 탐색
from collections import deque
name="ABCDEF"
arr=[
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

def bfs(start):
    q=deque()
    q.append(start)
    while q:
        now=q.popleft()
        print(name[now],end=' ')
        for i in range(6):
            if arr[now][i]==1:
                q.append(i)
bfs(0)  # 시작 인덱스
'''
'''
# 그래프탐색 (BFS) _ 트리모양이 아니고 모든 정점 1번씩만 탐색
from collections import deque
name = 'BACD'
arr =[
    [0,0,0,1],
    [1,0,1,0],
    [0,0,0,1],
    [0,0,0,0],
]
used = [0] * 4
used[1] = 1
def bfs(num):
    q = deque()
    q.append(num)
    while q:
        now = q.popleft()
        print(name[now],end=' ')
        for i in range(4):
            if arr[now][i] == 1 and used[i] == 0:
                used[i] = 1
                q.append(i)

bfs(1)
'''
'''
# 한 정점에서 다른 정점까지 갈수있는 방법은 몇가지? BFS 풀이
from collections import deque
import copy
name="ABCD"
arr=[
    [0,1,1,0],
    [0,0,1,1],
    [0,1,0,1],
    [0,0,0,0]]

cnt=0
def bfs(start):
    global cnt
    q=deque()
    used = [0] * 4
    used[start] = 1
    q.append((start,used))

    while q:
        now = q.popleft()
        if now[0] == 3:
            cnt += 1

        for i in range(4):
            if arr[now[0]][i] == 1 and now[1][i] == 0:
                tmp = copy.deepcopy(now[1])
                tmp[i] = 1
                q.append((i,tmp))

bfs(0)
print(cnt)
'''
'''
# Flood Fill, Virus
from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]
y,x = map(int,input().split())
arr[y][x] = 1
q = deque()
q.append((y,x))
directY = [0,0,1,-1]
directX = [1,-1,0,0]

while q:
    y,x = q.popleft()
    for i in range(4):
        dy = y + directY[i]
        dx = x + directX[i]
        if dy < 0 or dy > n - 1 or dx < 0 or dx > n - 1:
            continue
        if arr[dy][dx] != 0:
            continue
        arr[dy][dx] = arr[y][x] + 1
        q.append((dy,dx))

for i in arr:
    print(*i)
'''
'''
# N 입력받은 후 N x N 사이즈의 맵에 바이러스를 투입해 보자고 합니다.
from collections import deque
N = int(input())
y,x = map(int,input().split())
arr = [[0] * N for _ in range(N)]
q = deque()
q.append((y,x,1))   # 좌표와 level
arr[y][x] = 1
directY = [0,0,1,-1]
directX = [1,-1,0,0]
ans = 0

while q:
    y,x,level = q.popleft()
    for i in range(4):
        dy = y + directY[i]
        dx = x + directX[i]
        if dy<0 or dy>N-1 or dx<0 or dx>N-1:
            continue
        if arr[dy][dx] != 0:
            continue
        arr[dy][dx] = arr[y][x] + 1
        q.append((dy,dx,level+1))

        if dy == 0 and dx == 1:
            ans = level+1
            break

print(ans)
'''
# 5*5 바이러스 2곳 입력받는 문제 - 민코딩 37.1

'''
# 미로찾기
from collections import deque
arr =[
    [0,0,0,0],
    [1,1,1,1],
    [1,0,1,0],
    [0,0,0,0],
]

q = deque()
q.append((0,0))
directY = [0,0,1,-1]
directX = [1,-1,0,0]
visited = [[0] * 4 for _ in range(4)]
visited[0][0] = 1
flag = 0

while q:
    y,x = q.popleft()
    for i in range(4):
        dy = y + directY[i]
        dx = x + directX[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 3:
            continue
        if arr[dy][dx] == 1:
            continue
        if visited[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        q.append((dy,dx))
        if dy == 3 and dx == 3:
            flag = 1
            break

if flag:
    print("탈출가능")
else:
    print("불가능")
'''