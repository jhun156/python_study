# Topology sort 위상정렬 'bfs'
# 작업순서
# 사이클이 있을 땐 사용 못함

from collections import deque

name = ['CS','language','project','algo','data_structure','cote','developer']   # 7개
arr = [
    [0,0,1,0,0,0,0],
    [0,0,0,1,1,0,0],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0],
]
acc = [0] * 7
used = [0] * 7
q = deque()

for j in range(7):
    for i in range(7):
        if arr[i][j] == 1:
            acc[j] += 1     # 세로로 1 찿아서 더하기

# 사전작업없이 바로 시작할 수 있는 작업은 q넣고 used에 1체크
for i in range(7):
    if acc[i] == 0:
        used[i] = 1
        q.append(i)

# bfs돌리면서 작업순서 q에 넣기
while q:
    now = q.popleft()
    print(name[now],end=' ')
    for i in range(7):
        if arr[now][i] == 1 and used[i] == 0:
            if acc[i] == 1:
                acc[i] = 0
                used[i] = 1
                q.append(i)
            else:
                acc[i] -= 1

'''
DFS
1. 그래프탐색
2. Backtracking
3. 완전탐색 Brute-Force

BFS
1. 그래프탐색
2. 완전탐색
3. FloodFill (Virus, Bloom)
'''




















