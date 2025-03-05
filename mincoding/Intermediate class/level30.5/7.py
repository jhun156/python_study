arr = list(map(int,input().split()))
cnt = 0

def dfs(n,level):

    global cnt
    if level == n:
        Sum = sum(path)
        if 10 <= Sum <= 20:
            cnt += 1
            return
        return

    for i in range(5):
        if used[i] == 0:
            used[i] = 1
            path[level] = arr[i]
            dfs(n,level+1)
            used[i] = 0

for i in range(2,6):
    path = [0] * i
    used = [0] * 5
    dfs(i,0)

print(cnt)