# import sys
# sys.stdin = open("input.txt","r")

L = int(input())
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# arr = [[2,4],[7,8],[6,9]]
abs_arr = []
for i in range(N):
    tmp = arr[i][1] - arr[i][0]
    abs_arr.append(tmp)

Max = max(abs_arr)
expectation = abs_arr.index(Max)
expectation += 1

cake = [0] * (L+1)
for i in range(N):
    for j in range(arr[i][0],arr[i][1]+1):
        if cake[j] == 0:
            cake[j] = i + 1

result_lst = []
for i in range(1,N+1):
    tmp = cake.count(i)
    result_lst.append(tmp)

real_Max = max(result_lst)
real = result_lst.index(real_Max)
real += 1

print(expectation)
print(real)