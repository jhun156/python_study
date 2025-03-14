# ATM

# N = int(input())
# P = list(map(int,input().split()))
# P.sort()
# Sum = 0
#
# for i in range(N):
#     Sum += P[i] * (N - i)
# print(Sum)

# Party-room

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[1])             # 파티가 끝나는 시간을 기준으로 정렬

cnt = 0
ans = 1
a,b = arr[0]

while cnt < N:

    x, y = arr[cnt]
    if x >= b:
        a,b = x,y
        ans += 1
    cnt += 1

print(ans)