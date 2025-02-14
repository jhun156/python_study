import sys
sys.stdin = open("input.txt","r")

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    lst = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                lst[i].append(1)
            else:
                lst[i].append(lst[i - 1][j - 1] + lst[i - 1][j])
    print(f'#{test}')
    for i in lst:
        print(*i)