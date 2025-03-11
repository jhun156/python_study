import sys
sys.stdin = open("input.txt","r")

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j].isdigit():
            arr[i][j] = int(arr[i][j])

