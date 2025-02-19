import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    sty = stx = edy = edx = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sty,stx = i,j
                break
            if arr[i][j] == 3:
                edy,edx = i,j
                break

    directY = [0,0,1,-1]
    directX = [1,-1,0,0]
    visited = [[0] * N for _ in range(N)]
    visited[sty][stx] = 1
    flag = 0

    def dfs(nowy,nowx):

        global flag
        if nowy == edy and nowx == edx:
            flag = 1
            return

        for i in range(4):
            dy = nowy + directY[i]
            dx = nowx + directX[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
                continue
            if arr[dy][dx] == 1 or visited[dy][dx] == 1:
                continue
            visited[dy][dx] = 1
            dfs(dy,dx)
            visited[dy][dx] = 0
            if flag:
                return

    dfs(sty,stx)
    print(f"#{tc} {flag}")