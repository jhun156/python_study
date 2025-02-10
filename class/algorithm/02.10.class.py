# 위아래좌우 좌표들의 합이 가장 큰 곳의 합과. 좌표값 출력하기
'''
arr=[[1,2,3,4],
    [1,2,9,4],
    [1,9,3,9],
    [1,2,9,4]]

def find_max(y,x):
    directX = [0,0,1,-1]
    directY = [1,-1,0,0]
    sum = 0
    for i in range(4):
        dx = x + directX[i]
        dy = y + directY[i]
        if 0 <= dy <= 3 and 0 <= dx <= 3:
            sum += arr[dy][dx]
    return sum,y,x

Max = 0
ans_y, ans_x = 0,0
for i in range(4):
    for j in range(4):
       tmp,Y,X = find_max(i,j)
       if Max < tmp:
           Max = tmp
           ans_y,ans_x = Y,X

print(f"Max={Max}, (y,x) = ({ans_y},{ans_x})")
'''
'''
import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    Max = 0
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    def find_max(y,x):
        directY = [0,0,1,-1]
        directX = [1,-1,0,0]
        Sum = 0
        for i in range(4):
            dy = y + directY[i]
            dx = x + directX[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
                return 0
            Sum += arr[dy][dx]
        Sum = Sum - arr[y][x]
        if Sum - arr[y][x] < 0:
            return 0
        elif Sum % 2 == 0:
            return Sum * 2
        else:
            return Sum

    for i in range(N):
        for j in range(N):
            ans = find_max(i,j)
            if Max < ans:
                Max = ans
    print(f"#{tc} {Max}")
'''

# 이진 탐색 (Binary Search)

def binary_search(st,ed,target):

    while True:
        mid = (st + ed) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            ed = mid - 1
        elif arr[mid] < target:
            st = mid + 1
        if st > mid:
            return 0

# Parametric Search
'''
battery="##########"

def parametric_search(st,ed):
    Max = -1
    while 1:
        mid = (st + ed) // 2
        if battery[mid] == "#":
            Max = mid
            st = mid + 1
        elif battery[mid] == "_":
            ed = mid - 1
        if st > ed:
            break
    return Max + 1

ans = parametric_search(0,9) * 10
print(f"{ans}%")
'''
# 워드작업 중 정전으로 인하여 컴퓨터가 강제로 종료가 되었습니다.
# 다시 전기가 들어와 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# 우리는 자동복구가 되었을때 커서의 위치가 어디인지를 알려줘야 합니다.
# 커서의 위치를 알려주는 프로그래밍을 완성해 주세요.
# 시간복잡도 (On^2)보다 빨라야 합니다.
'''
# 6*10 size 리스트 (배열)
curser=[
    '##########',
    '##########',
    '###_______',
    '__________',
    '__________',
    '__________']

def binary_search(start,end):
    Max=-1
    while 1:
        mid=(start+end)//2
        if curser[mid][0]=='_':
            end=mid-1
        elif curser[mid][0]=='#':
            Max=mid
            start=mid+1
        if start>end:
            break
    return Max+1

def binary_search2(start,end,y):
    Max=-1
    while 1:
        mid=(start+end)//2
        if curser[y][mid]=='_':
            end=mid-1
        elif curser[y][mid]=='#':
            Max=mid
            start=mid+1
        if start>end:
            break
    return Max+1

yaxis=binary_search(0,5)
yaxis-=1
xaxis=binary_search2(0,9,yaxis)
print(yaxis,xaxis)
'''

# 재귀호출 (재귀 함수, Recursion)
# 어떠한 함수가 자기자신을 계속 호출하는 함수
'''
def abc(level):

    if level == 2:
        print(level)
        return
    print(level)
    abc(level+1)
    print(level)
    
abc(0)
'''

# 5 입력시 0 1 2 3 4 4 3 2 1 0
# 3 입력시 0 1 2 2 1 0

def abc(level):

    if level == 5:
        return

    print(level)
    abc(level+1)
    print(level)

abc(0)




















