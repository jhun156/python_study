# import sys
# sys.stdin = open("input.txt","r")

T, N = map(int,input().split())
coins = list(map(int,input().split()))
DP = [21e8] * (T+1)
DP[0] = 0

def find(n):

    for coin in coins:
        for i in range(coin,T+1):
            DP[i] = min(DP[i], DP[i-coin] + 1)

    if DP[n] != 21e8:
        return DP[n]
    else:
        return "impossible"

print(find(T))