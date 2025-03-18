import sys
sys.stdin = open("input.txt","r")

'''
N, K = map(int,input().split())
used = [0] * N
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

Max = -21e8

def dfs(kg,value):

    global Max
    for i in range(N):
        if used[i] == 0 and kg - arr[i][0] >= 0:
            used[i] = 1
            dfs(kg-arr[i][0], value+arr[i][1])
            used[i] = 0

    Max = max(Max,value)

dfs(K,0)
print(Max)
'''
'''
# 민환
N,K=map(int,input().split())
lst=[]
Max=0
for i in range(N):
    W,V=map(int,input().split())
    lst.append((W,V))
for i in range(1<<N):
    value=0
    weigh=0
    for j in range(N):
        if i&(1<<j):
            weigh+=lst[j][0]
            value+=lst[j][1]
            if weigh>K:
                break
        if value>Max:
            Max=value
print(Max)
'''

# 강사님 DP 코드
n,k=map(int,input().split())
knapsack=[[0 for _ in range(k+1)] for _ in range(n+1)]
item=[[0,0]]
for i in range(1,n+1):
    item.append(list(map(int,input().split())))
# 배열에 값 채워 넣기
for i in range(1,n+1): # 물건종류
    for j in range(1,k+1): # 가방무게
        weight=item[i][0]
        value=item[i][1]

        if j<weight: # 물건무게 > 여유있음가방무게
            knapsack[i][j]=knapsack[i-1][j] # 그전 단계에서 구했던 값으로 갱신
        else: # 가방에 물건을 넣을 수 있는경우
            knapsack[i][j]=max(knapsack[i-1][j], value+knapsack[i-1][j-weight])
            # 그전 단계에서 구했던 최대효율 vs 지금물건 1개 넣은것 + 남은 무게 (그전단계에서 구한)

print(knapsack[n][k])


