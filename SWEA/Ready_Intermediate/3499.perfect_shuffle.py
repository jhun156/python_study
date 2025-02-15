# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr1 = list(input().split())
    n = N // 2
    arr2 = arr1[N-n:]
    del arr1[N-n:]
    # arr1,arr2 라는 2개의 덱으로 나눔
    ans_result = []
    for i in range(n):
        ans_result.append(arr1.pop(0))
        ans_result.append(arr2.pop(0))
        # ans_result에 arr1, arr2 순서대로 0번 인덱스 값을 추가함
    if arr1:
        ans_result.append(arr1.pop())
        # N이 홀수인 경우 arr1에는 하나의 원소가 남아있기 때문에 마지막에 추가
    print(f"#{tc}",end=' ')
    print(*ans_result)