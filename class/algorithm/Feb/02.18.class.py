# 재귀호출 경로 저장하면서 탐색
'''
name = 'ABC'
path = [0] * 2

def abc(level):
    if level == 2:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return

    for i in range(3):
        path[level] = name[i]
        abc(level + 1)
        path[level] = 0

abc(0)
'''
'''
path = [0] * 2

def abc(level):

    if level == 2:
        print(*path)
        return

    for i in range(6):
        path[level] = i + 1
        abc(level+1)
        #path[level] = 0     해도 되고 안해도 상관없음

abc(0)
'''
# 순열
# 3장을 뽑았을 때 나올 수 있는 경우 모두 출력

card='ABCD'
path=[0]*3
used=[0]*4
def abc(level):
    if level == 3:
        print(*path)
        return

    for i in range(4):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = card[i]
        abc(level+1)
        used[i] = 0

abc(0)