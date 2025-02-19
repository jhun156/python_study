'''
# stack (Last In First Out, LIFO)
st=list()
st.append(2)
st.append(3)
st.append(4)
st.append(5)    # st = [2,3,4,5]

test = st.pop()
st.pop()
print(st)       # [2,3]

# stack은 append, pop 으로 쉽게 구현 가능

# Queue (First In First Out, FIFO)
q=list()
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)         # [3,4,5,6,7]
q.pop(0)            # O = 1
test = q.pop(0)     # pop(0), O = n
print(q)            # [5,6,7]

from collections import deque
q = deque()
q.append(5)
q.append(15)
q.append(25)
q.append(35)
q.append(45)
print(q)        # deque([5, 15, 25, 35, 45])
print(list(q))  # [5, 15, 25, 35, 45]

q.popleft()
q.popleft()
print(list(q))  # [25, 35, 45]

import queue        # 잘 안씀. 참고용
q = queue.Queue()
q.put(5)
q.put(15)
q.put(25)   # 추가할 땐 put
q.get()     # 제거할 땐 get
print(q)
print(q.queue)
'''
# DFS

# 트리구조
# 1. 부모 관계, 2. 단방향
# 사이클 발생 X
# 맨 위의 노드를 root node
# 가장 아래 노드를 leaf node

# 트리 구조를 소스코드로 옮기는 방법
# 1. 인접 행렬, 2. 인접 리스트 3. 1차원 리스트 (이진 트리의 경우)

# 1. 인접 행렬
# 010010
# 001100 방식

# 2. 인접 리스트
# [[1,4]
#  [2,3]] 방식
'''
name="ABCDEF"
arr=[
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

def dfs(now):
    print(name[now],end=' ')
    for x in range(6):
        if arr[now][x]==1:
            dfs(x)

dfs(0) # 트리 탐색을 할 인덱스 적어주기
'''

'''
# tree를 인접리스트로 표현 후 DFS 탐색하기
import sys
sys.stdin = open("input.txt","r")

name="ABCDEF"
N,M = map(int,input().split())
arr = [[] for _ in range(N)]
for i in range(M):
    si,do = map(int,input().split())
    arr[si].append(do)

def dfs(now):

    print(now, end=' ')
    for i in arr[now]:
        dfs(i)

dfs(0)
'''

'''
# Tree 구조가 아닐때 visited를 활용하는 법
name = 'ACBD'
arr =[
    [0,1,1,0],
    [1,0,0,1],
    [0,1,0,1],
    [0,0,0,0],
]

visited = [0] * 4
visited[0] = 1

def dfs(now):

    print(name[now],end='')
    for i in range(4):
        if arr[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

dfs(0)
'''

'''
# 경로 갯수 검색
name = 'ABCD'
arr = [
    [0,1,1,0],
    [0,0,1,1],
    [0,1,0,1],
    [0,0,0,0],
]
visited = [0] * 4
visited[0] = 1
cnt = 0

def dfs(now):

    global cnt
    if now == 3:
        cnt += 1
    for i in range(4):
        if visited[i] == 0 and arr[now][i] == 1:
            visited[i] = 1
            dfs(i)
            visited[i] = 0

dfs(0)
print(cnt)
'''

'''
# 가중치가 있는 경로 탐색
arr = [
    [0,1,8,0],
    [0,0,1,7],
    [0,1,0,1],
    [0,0,0,0],
]
visited = [0] * 4
visited[0] = 1
Min = 21e8

def dfs(now,Sum):

    global Min
    if now == 3:
        Min=min(Min,Sum)

    for i in range(4):
        if visited[i] == 0 and arr[now][i] != 0:
            visited[i] = 1
            dfs(i,Sum+arr[now][i])
            visited[i] = 0

dfs(0,0)
print(Min)
'''

'''
# 미로 찾기

maze = [
    [0,0,0,0,0],
    [0,0,1,1,0],
    [1,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
]
visited = [[0] * 5 for _ in range(5)]
flag = 0
directY = [0,0,1,-1]
directX = [1,-1,0,0]

def dfs(nowy,nowx):

    global flag
    if nowy == 3 and nowx == 2:
        flag = 1
        return

    for i in range(4):
        dy = nowy + directY[i]
        dx = nowx + directX[i]
        if dy < 0 or dy > 4 or dx < 0 or dx > 4:
            continue
        if maze[dy][dx] == 1:
            continue
        if visited[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        dfs(dy,dx)
        if flag:
            return

visited[0][0] = 1
dfs(0,0)
if flag:
    print("가능")
else:
    print("불가능")
'''

'''
# 한 지점에서 다른 지점으로 최소 이동거리 구하기
arr = [
    [0,0,0,0,1],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,0,0],
    [1,0,0,0,0],
]

visited = [[0] * 5 for _ in range(5)]
Min = 21e8
directY = [0,0,1,-1]
directX = [1,-1,0,0]
cnt = 0

def dfs(nowy,nowx,level):

    global Min,cnt
    if nowy == 4 and nowx == 2:
        Min = min(level,Min)
        cnt = 0
        return

    for i in range(4):
        dy = nowy + directY[i]
        dx = nowx + directX[i]
        if dy < 0 or dy > 4 or dx < 0 or dx > 4:
            continue
        if arr[dy][dx] == 1:
            continue
        if visited[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        dfs(dy,dx,level+1)
        visited[dy][dx] = 0

visited[0][0] = 1
dfs(0,0,0)
print(Min)
'''













