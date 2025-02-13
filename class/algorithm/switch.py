# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if arr[i] != lst[i]:
            for j in range(i, N):
                arr[j] = 1 - arr[j]
            cnt += 1
    print(f"#{tc} {cnt}")