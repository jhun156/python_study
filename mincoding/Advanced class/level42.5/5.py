# import sys
# sys.stdin = open("input.txt","r")

N = 6
arr = list(map(int,input().split()))
L = int(input())
Max = -21e8
count = 0

def dfs(level,cnt,Sum):

    global Max,count
    count += 1
    if level == L:
        Max = max(Sum,Max)
        return

    if cnt % 3 == 0:
        for i in range(3):
            tmp = arr[i]
            arr[i] = 0
            dfs(level,cnt+1,Sum+tmp)
            arr[i] = tmp
    if cnt % 3 == 1:
        for j in range(3,6):
            tmp = arr[j]
            arr[j] = 0
            dfs(level,cnt+1,Sum+tmp)
            arr[j] = tmp
    if cnt % 3 == 2:
        for k in range(1,5):
            tmp = arr[k]
            arr[k] = 0
            for x in range(6):
                if arr[x] != 0:
                    arr[x] *= 2
            dfs(level+1,cnt+1,Sum+tmp)
            for x in range(6):
                if arr[x] != 0:
                    arr[x] //= 2
            arr[k] = tmp


dfs(0,0,0)
print(Max)
print(count)