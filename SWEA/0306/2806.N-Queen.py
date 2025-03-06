import sys
sys.stdin = open("input.txt","r")
from copy import deepcopy

T = int(input())
for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    used = [0] * N

    def dfs(level):

        global cnt
        if level == N:
            cnt += 1
            return




    dfs(0)
    print(f"#{tc} {cnt}")