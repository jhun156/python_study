# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    check_lst = [list(map(int,input().split())) for _ in range(M)]

    def check(x,num):
        x -= 1
        for i in range(1,num+1):
            left = x - i
            right = x + i
            if left < 0 or right > N - 1:
                return
            if arr[left] == arr[right]:
               arr[left] = 1 - arr[left]
               arr[right] = 1 - arr[right]
        return

    for i in range(M):
        check(check_lst[i][0],check_lst[i][1])

    print(f"#{tc}", *arr)