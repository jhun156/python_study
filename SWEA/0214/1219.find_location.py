import sys
sys.stdin = open("input.txt","r")

T = 10
for tc in range(1,T+1):
    T,N = map(int,input().split())
    arr = list(map(int,input().split()))
    connect = [[] for _ in range(N+1)]
    for i in range(0,N*2,2):
        connect[arr[i]].append(arr[i+1])
    visited = [0] * 100

    def dfs(s,g):
        stack = [s]
        visited[s] = 1

        while 1:
            now = stack.pop()
            if now == g:
                return 1

            for next_node in connect[now]:
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    stack.append(next_node)

            if not stack:
                return 0

    ans = dfs(0,99)
    print(f"#{tc} {ans}")