'''
# 집합 123 에서 모든 순열을 생성하는 함수
for i1 in range(1,4):
    for i2 in range(1,4):
        if i1 != i2:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1,i2,i3)

def backtrack(a,k,n):
    c = [0] * MAXCANDIDATES

    if k == n:
        for i in range(0,k):
            print(a[i],end=' ')
        print()
    else:
        ncandidates = construct_candidates(a,k,n,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k)
'''

# 순열 문제에서의 가지치기
# 4881.배열 최소 합

card="ABCD"
path=[0]*3
used=[0]*4
def abc(level):
    if level==3:
        print(*path)
        return

    for i in range(4):
        if used[i]==1: continue
        used[i]=1
        path[level]=card[i]
        abc(level+1)
        used[i]=0

abc(0)













