# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
switch = list(map(int,input().split()))
P = int(input())
arr = [list(map(int,input().split())) for _ in range(P)]

for i in range(P):
    if arr[i][0] == 1:  # 남학생
        for j in range(N):
            if (j+1) % arr[i][1] == 0:
                switch[j] = 1 - switch[j]
    else:
        tmp = arr[i][1] - 1
        switch[tmp] = 1 - switch[tmp]
        for j in range(1,N):
            if tmp - j < 0 or tmp + j >= N:
                break
            if switch[tmp-j] != switch[tmp+j]:
                break
            else:
                switch[tmp-j] = 1 - switch[tmp-j]
                switch[tmp+j] = 1 - switch[tmp+j]

B = N // 20 + 1
for i in range(B):
    print(*switch[i*20:(i+1)*20])
