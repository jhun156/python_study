N = int(input())
arr = list(map(int,input().split()))
path = [0] * (N-1)
name = ['!!','#','$','&']
cnt = 0

def dfs(level):
    global cnt
    if level == N - 1:
        tmp = arr[0]
        for i in range(N-1):
            if path[i] == '!!':
                tmp = (tmp-arr[i+1]) * (tmp+arr[i+1])
            elif path[i] == '#':
                tmp = max(tmp,arr[i+1])
            elif path[i] == '$':
                tmp = tmp ** 2 - arr[i+1] ** 2
            elif path[i] == '&':
                tmp = (tmp+arr[i+1]) ** 2
        if tmp == 100:
            cnt += 1
        return

    for i in range(4):
        path[level] = name[i]
        dfs(level+1)

dfs(0)
print(cnt)