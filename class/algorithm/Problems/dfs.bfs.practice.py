'''
# DFS 거스름돈 동전 최소 개수 구하기
changes=int(input())
coin=[110,70,10]
Min=21e8

def dfs(level,money):
    global Min
    if money<0 or level>Min: # 거슬러줄돈이 음수거나
                             # 최소사용동전개수를 초과할경우
        return

    if money==0:
        Min=min(Min,level)
        return
    for i in range(3):
        dfs(level+1,money-coin[i])
dfs(0,changes)  # level 거슬러줄돈
print(Min)
'''

# line1=[5,2,7,-5,-7,9]
# line2=[4,-5,-7,9,-5,3]
# 두 라인에서 숫자 1개씩 번갈아 가며 선택할때
# 라인1에서 1개 라인2에서 1개... 번갈아 가며 뽑습니다.
# (각 라인의 숫자는 1번씩만 사용하며 숫자를 뽑습니다.)
# 첫 번째 숫자 선택한 값에 *1 을하고
# 두번째 택한 값에 *2를 하고
# 세번째 택한 값에 *3.. 씩
# 모든 값에 1씩 증가되는 값으로 가중치를 곱한 후
# 모두 더했을떄 0에 가장 가까운 수를 구하고자 합니다.
# 이때 총 합이 몇이 될까요??

'''
line1 = [5,2,7,-5,-7,9]
line2 = [4,-5,-7,9,-5,3]
used1 = [0] * 6
used2 = [0] * 6
Min = 21e8

def dfs(level,Sum):

    global Min
    if level == 12:
        if abs(Min) > abs(Sum):
            Min = Sum
            return

    if level % 2 == 0:
        for i in range(6):
            if used1[i] == 0:
                used1[i] = 1
                dfs(level+1,Sum+(line1[i]*(level+1)))
                used1[i] = 0
    else:
        for i in range(6):
            if used2[i] == 0:
                used2[i] = 1
                dfs(level+1,Sum+(line2[i]*(level+1)))
                used2[i] = 0

dfs(0,0)
print(Min)
'''
'''
# 서바이벌 선수와 전투력이 있을때
# a~f를 두 팀으로 만들어서 서바이벌 게임을 하고자 한다.
# 두 팀의 전투력 차이가 가장 적게하여 두 팀을 구성한다고 했을때
# 두 팀의 최소 전투력 차이는 몇이 되는가?
# 모든 선수는 서바이벌에 참가하며 1인팀도 가능합니다.

power = [50,40,99,5,25,6,37]
Min = 21e8
used = [0] * 7

def dfs(n,level,Sum):

    global Min
    if level == n:
        tmp = abs((sum(power)-Sum)-Sum)
        if Min > tmp:
            Min = tmp
            return

    for i in range(7):
        if used[i] == 0:
            used[i] = 1
            dfs(n,level+1,Sum+power[i])
            used[i] = 0

for i in range(1,4):
    dfs(i,0,0)

print(Min)
'''

'''
# 강사님 풀이
power = [50,40,99,5,25,6,37]
Min = 21e8
total = sum(power)

def dfs(level,start,Sum):

    global Min
    against = total - Sum
    gap = abs(Sum-against)
    Min = min(gap,Min)

    if level == 6:
        return

    for i in range(start,7):
        dfs(level+1,i+1,Sum+power[i])

dfs(0,0,0)
print(Min)
'''
from copy import deepcopy

arr = [
    [3,1,9,6],
    [6,5,9,6],
    [5,8,3,7],
]
Max = -21e8

def dfs(level):

    global Max, arr
    if level == 4:
        Sum = 0
        for i in range(3):
            for j in range(4):
                Sum += arr[i][j]

        Max = max(Max,Sum)
        return

    backup = deepcopy(arr)

    for i in range(12):
        directY = [0,0,0,1,-1]
        directX = [0,1,-1,0,0]
        y = i // 4
        x = i % 4
        for j in range(5):
            dy = directY[j] + y
            dx = directX[j] + x
            if dy < 0 or dy > 2 or dx < 0 or dx > 3: continue
            arr[dy][dx] = (arr[dy][dx] * 7) % 10
        dfs(level+1)
        arr = deepcopy(backup)

dfs(0)
print(Max)


























