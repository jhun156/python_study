N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [0] * N
saw = set()
saw.add(tuple(visited))
Max = -1
cnt = 1

def dfs():

    global arr, Max, cnt

    value = 1
    for j in range(N):
        tmp = 0
        for i in range(N):
            tmp += arr[i][j]
        value *= tmp
    Max = max(Max,value)

    for i in range(N):
        if visited[i] < N - 1:
            visited[i] += 1
            tmp = tuple(visited)
            if tmp not in saw:
                saw.add(tmp)
                rotation(arr[i])
                print(cnt, end=' ')
                cnt += 1
                dfs()
                visited[i] -= 1


def rotation(lst):
    lst.insert(0,lst.pop())

dfs()
print(f"{Max}점")