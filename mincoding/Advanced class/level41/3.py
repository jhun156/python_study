# import sys
# sys.stdin = open("input.txt","r")

T, N = map(int,input().split())
coins = list(map(int,input().split()))
arr = [21e8] * (T+1)
coins.sort()

for coin in coins:
    start = coin
    for j in range(start,T+1):
        if j % coin == 0:
            arr[j] = j // coin
        else:
            arr[j] = min(arr[j],j//coin + arr[j%coin])

if arr[T] == 21e8:
    print("impossible")
else:
    print(arr[T])