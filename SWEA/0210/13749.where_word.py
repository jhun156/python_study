import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    Sum = 0
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(arr[i][j])
        lst.append(row)
    for j in range(N):
        row = []
        for i in range(N):
            row.append(arr[i][j])
        lst.append(row)

    def find_K(arr):
        for i in range(N-K+1):
            Sum = 0
            for j in range(K):
                Sum += arr[i+j]
        return Sum

    for i in range(2*N):
        pass


    print(f"#{tc} {Sum}")
