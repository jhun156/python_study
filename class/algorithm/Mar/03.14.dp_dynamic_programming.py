# 동적계획법
# 1. TOP-DOWN 방식
# 2. BOTTON-UP 방식

# 피보나치 수열
# ex) top-down

# memo = [-1] * 5
# memo[0] = 0
# memo[1] = 1
#
# def fibo(n):
#
#     if memo[n] != -1:
#         return memo[n]
#
#     if n <= 1:
#         return
#
#     memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]
#
# fibo(4)
# print(*memo)

# ex) bottom-up

'''
def fibo(n):

    global dp
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]


dp = [0] * 5
dp[0] = 0
dp[1] = 1
fibo(4)
print(*dp)
'''
'''
# 개구리 점프
arr = list(map(int,input().split()))
N = len(arr)

def jump():

    score = [-1000] * N
    score[0] = 0
    for i in range(1,N):
        tmp = []
        a = score[i-1] + arr[i]
        tmp.append(a)
        if i >= 2:
            b = score[i-2] + arr[i]
            tmp.append(b)
        if i % 2 == 0 and i != 0:
            c = score[i//2] + arr[i]
            tmp.append(c)
        score[i] = max(tmp)

    return score[N-1]

result = jump()
print(result)
'''
'''
arr = [
    [0,5,3,6,8],
    [1,4,2,9,1],
    [6,9,1,7,7],
    [8,5,4,1,0],
]
cost = [[0] * 5 for _ in range(4)]

def find_cost(y,x):

    global cost
    dY = [-1,0]
    dX = [0,-1]
    result = []
    for i in range(2):
        dy = y + dY[i]
        dx = x + dX[i]
        if dy < 0 or dx < 0:
            continue
        tmp = cost[dy][dx]
        result.append(tmp)

    if not result:
        return 0
    else:
        return min(result)+arr[y][x]

for i in range(4):
    for j in range(5):
        cost[i][j] = find_cost(i,j)

print(cost[3][4])
'''




























