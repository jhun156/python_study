N = int(input())
arr = list(map(int,input().split()))
visited = [0] * N
path = [0] * N
ans = 0
Max = -1111

def fire(num):

    if num - 1 >= 0:
        visited[num-1] += 1
    if num + 1 <= N - 1:
        visited[num+1] += 1
    visited[num] += 1

def water(num):

    if num - 1 >= 0:
        visited[num - 1] -= 1
    if num + 1 <= N - 1:
        visited[num + 1] -= 1
    visited[num] -= 1

def dfs(level,Sum):

    global Max, path, ans
    tmp = visited.count(0)
    if tmp == 0:
        if Sum > Max:
            Max = Sum
            ans = path[:level]

    for i in range(N):
        if visited[i] != 0: continue
        fire(i)
        path[level] = arr[i]
        dfs(level+1,Sum+arr[i])
        water(i)


dfs(0,0)
print(ans[0],end='')
for i in range(1,len(ans)):
    print('+',end='')
    print(ans[i],end='')
print('=',end='')
print(Max)