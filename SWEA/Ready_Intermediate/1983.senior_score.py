# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    K -= 1
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        arr[i] = arr[i][0] * 0.35 + arr[i][1] * 0.45 + arr[i][2] * 0.2

    arr2 = [0] * N
    tmp = N - 1
    for i in range(N):
        index = arr.index((max(arr)))
        arr2[index] = tmp
        tmp -= 1
        arr[index] = 0
    # arr2 = arr의 각 원소의 총점을 정수로 전환한 리스트
    value = arr2[K]
    arr3 = sorted(arr2,reverse=True)
    ret = arr3.index(value)
    score_list = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

    tmp = N // 10
    mul = 0
    while 1:
        if ret - mul * tmp < 0:
            break
        else:
            mul += 1

    print(f"#{tc} {score_list[mul-1]}")