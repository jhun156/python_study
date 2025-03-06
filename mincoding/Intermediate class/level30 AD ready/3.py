import sys
sys.stdin = open("input.txt","r")

name = 'ABCDEF'
arr = [list(map(int,input().split())) for _ in range(6)]
path = [0]
used = [0]*6
used[0] = 1

def dfs(num):

    for i in range(6):
        if arr[num][i] == 1:
            path.append(i)
            dfs(i)
            path.pop()

    for i in range(len(path)):
        print(name[path[i]],end='')
    print()

    if len(path) == 1:
        return

dfs(0)