# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    arr = [0] * (N+1)
    for i in range(M):
        idx,value = map(int,input().split())
        arr[idx] = value

    for i in range(N,0,-1):
        if 2*i > N:
            continue
        elif 2*i == N:
            arr[i] = arr[2*i]
        else:
            arr[i] = arr[2*i] + arr[2*i+1]

    print(f"#{tc} {arr[L]}")