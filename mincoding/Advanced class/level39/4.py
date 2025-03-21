N = int(input())
length = list(map(int,input().split()))
length.sort()

wood = 100
ans = 0
for i in range(N):
    wood -= length[i]
    if wood < 0:
        ans = i - 1
        break

print(ans+1)