# import sys
# sys.stdin = open("input.txt","r")

t = int(input())

for test_case in range(1, t + 1):
    K, N, M = map(int, input().split())
    charge_stop = list(map(int, input().split()))

    start,cnt = 0,0
    tmp = start + K
    while start + K < N:
        for i in range(M-1,-1,-1):
            if tmp == charge_stop[i]:
                start = tmp
                tmp = start + K
                cnt += 1
                break
        else:
            tmp -= 1
        if tmp == start:
            cnt = 0
            break
    print(f"#{test_case} {cnt}")