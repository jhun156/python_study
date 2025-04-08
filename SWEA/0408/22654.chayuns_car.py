# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    Q = int(input())
    sty, stx, edy, edx = 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                sty, stx = i, j
            elif arr[i][j] == 'Y':
                edy, dex = i, j

    result = []
    for _ in range(Q):
        a, command = input().split()
        n = int(a)
        ny,nx = sty,stx
        present = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for i in range(n):
            if command[i] == 'R':
                present += 1
            elif command[i] == 'L':
                present -= 1
            elif command[i] == 'A':
                next = directions[present % 4]
                move_y = ny + next[0]
                move_x = nx + next[1]
                if move_y < 0 or move_y > N - 1 or move_x < 0 or move_x > N - 1:
                    continue
                if arr[move_y][move_x] == 'T':
                    continue
                ny,nx = move_y,move_x

        if arr[ny][nx] == 'Y':
            result.append(1)
        else:
            result.append(0)

    print(f"#{tc}", *result)