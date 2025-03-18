# 3
# 14

# 2차원 배열을 이용해서 하는 방법
# 패딩값을 넣어준다는게 이전까지의 코드와 다름

N = int(input())    # 동전 종류 개수
K = int(input())    # 거슬러받으려는 돈 액수
arr = [[0] * (K+1) for _ in range(N+1)]
for i in range(1,K+1):
    arr[0][i] = 1000

coin = [0,1,7,10]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j % coin[i] == 0:
            arr[i][j] = j // coin[i]
        else:
            if j // coin[i] == 0:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = min(arr[i-1][j],1+arr[i][j % coin[i]])

print(arr[3][14])
print(*arr)

# 강사님 코드
# 리스트 하나로도 풀이 가능

n,k=map(int,input().split())
coin=[]
for i in range(n):
    don=int(input())
    coin.append(don)
coin.sort()
arr=[1001]*(k+1)
arr[0]=0
for i in range(n):
    start=coin[i]
    for j in range(start,k+1):
        arr[j]=min(arr[j],arr[j-start]+1)
print(arr[k])