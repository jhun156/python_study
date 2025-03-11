# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    ans = -21e8
    st = 0

    while st < N - 1:
        cnt = 0
        ed = st + 1
        tmp = arr[st]
        while ed <= N - 1:
            if arr[ed] > tmp:
                cnt += 1
                tmp = arr[ed]
            ed += 1
        ans = max(ans,cnt)
        st += 1

    print(f"#{tc} {ans}")