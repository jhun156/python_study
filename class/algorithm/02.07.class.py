# DAT (Direct Address Table)
'''
a = [3,8,5,2,5,7,2,4]
n = int(input())
b = list(map(int,input().split()))
cnt = 0
for i in range(len(b)):
    cnt = 0
    for j in range(len(a)):
        if b[i] == a[j]:
            cnt += 1
    print(f"{b[i]} : {cnt}개 있음")
'''
'''
a = [3,8,5,2,5,7,2,4]
n = int(input())
b = list(map(int,input().split()))  #[1,2,3,4]
bucket = [0] * 10
'''

# n개의 숫자를 입력받은 후
# 어떠한 숫자가 몇개 입력이 되었는지 출력

# 1 1 2 3 1 2 6
'''
arr = [i for i in map(int,input().split())]
bucket = [0] * 8
for i in range(len(arr)):
    bucket[arr[i]] += 1
for i in range(len(bucket)):
    if bucket[i] != 0:
        print(f"{i} : {bucket[i]}")
'''

# 어떤 알파벳이 몇 개씩 사용되었는지 출력하기
'''
lst = list(input())
bucket = [0] * 26
# print(ord('a')) #97
for i in range(len(lst)):
    bucket[ord(lst[i])-97] += 1
for i in range(len(bucket)):
    if bucket[i] != 0:
        print(f"{chr(i+97)} : {bucket[i]}")
'''
# Counting Sort
# 1. DAT 2. 누적합 3. 값넣기
'''
n=int(input())
a=list(map(int,input().split()))
bucket=[0]*10

for i in a:
    bucket[i]+=1

for i in range(1,len(bucket)):
    bucket[i]+=bucket[i-1]

result=[0]*n
for i in range(n):
    bucket[a[i]]-=1
    index=bucket[a[i]]
    result[index]=a[i]
    
print(*result)
'''

# 연속되는 숫자 3개의 합이 가장 클 때의 값을 출력해주세요.
'''
lst = [[4,5,2,6,7,3,1],
       [2,9,9,6,1,6,7]]
rnt = 0
for i in range(2):
    for j in range(5):
        if lst[i][j] + lst[i][j+1] + lst[i][j+2] > rnt:
            rnt = lst[i][j] + lst[i][j+1] + lst[i][j+2]
print(rnt)
def getSum(y,x):
    Sum = 0
    for i in range(3):
        Sum += lst[y][x+i]
    return Sum

for i in range(2):
    for j in range(5):
        ret = getSum(i,j)
        if ret>Max:
            Max=ret
'''
'''
1 2 3 4 5
2 4 2 1 3
3 4 5 2 5
3 4 5 라는 패턴 찾기
'''
'''
arr = [
    [1,2,3,4,5],
    [2,4,2,1,3],
    [3,4,5,2,5],
]

def getPattern(y,x):
    rnt = 0
    for i in range(3):
        if arr[y][x+i] == 3 + i:
            rnt += 1
    return rnt

cnt = 0
for i in range(3):
    for j in range(3):
        ret = getPattern(i,j)
        if ret == 3:
            print(f"{i},{j}")
            cnt += 1

if cnt == 0:
    print("패턴없음")
'''

'''
1 5 4 2
1 3 4 2
3 5 3 2
2 6 4 1
'''
'''
arr = [
    [1,5,4,2],
    [1,3,4,2],
    [3,5,3,2],
    [2,6,4,1],
]
def ground(y,x):
    ret = 0
    for i in range(2):
        for j in range(3):
            ret += arr[y+i][x+j]
    return ret

result = 0
for i in range(3):
    for j in range(2):
        Max = ground(i,j)
        if Max > result:
            result = Max
print(result)
'''
'''
arr = [
    [3, 5, 4],
    [1, 1, 2],
    [1, 3, 9],
]
y, x = map(int, input().split())
Sum = 0
directX = [0,0,1,-1]
directY = [1,-1,0,0]
Sum = 0
for i in range(4):
    dx = x + directX[i]
    dy = y + directY[i]
    if dx > 2 or dx < 0 or dy > 2 or dy < 0:
        continue
    Sum += arr[dy][dx]
print(Sum)
'''
'''
# 파이썬만 가능한 방법
arr = [
    [3, 5, 4],
    [1, 1, 2],
    [1, 3, 9],
]
y, x = map(int, input().split())
Sum = 0
for i,j in (-1,0),(1,0),(0,-1),(0,1):
    dy,dx = y+i,x+j
    if 0<=dy<=2 and 0<=dx<=2:
        Sum += arr[dy][dx]
'''
arr = [
    [3, 5, 4, 5, 6],
    [1, 1, 2, 7, 8],
    [1, 2, 9, 1, 2],
    [3, 5, 4, 5, 6],
    [1, 1, 2, 7, 8],
]

y,x = map(int,input().split())
Sum = 0
directX = [1,-1,0,0]
directY = [0,0,1,-1]
for i in range(4):
    for j in range(1,4):
        dy = y + directY[i]*j
        dx = x + directX[i]*j
        if dx > 4 or dx < 0 or dy > 4 or dy < 0:
            continue
        Sum += arr[dy][dx]
print(Sum)




















