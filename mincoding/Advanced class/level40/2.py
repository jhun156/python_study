N = int(input())

def DP(num):

    if num == 1:
        return 1

    if num == 2:
        return 2

    return DP(num-1) + DP(num-2)

ans = DP(N)
print(ans)