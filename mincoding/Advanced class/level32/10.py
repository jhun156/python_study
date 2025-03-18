N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
bit = [list(map(int,input().split())) for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if bit[i][j] == 1:
            result.append(arr[i][j])

ans = [0] * len(result)
for i in range(len(result)):
    ans[i] = (result.count(result[i]), result[i])

ans.sort(key = lambda x: (-x[0],x[1]))
for i in range(len(ans)):
    print(ans[i][1],end=' ')