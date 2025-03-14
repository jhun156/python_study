# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
arr.append(0)
N += 2
score = [-21e8] * N
score[0] = 0

for i in range(2,N):
    if i < 7:
        score[i] = score[i-2] + arr[i]
    a = score[i-7] + arr[i]
    b = score[i-2] + arr[i]
    if a > b:
        score[i] = a
    else:
        score[i] = b

if N -8 >= 0:
    ans = max(score[N-8:N])
else:
    ans = max(score)
print(ans)