# 고지식한 패턴 검색 알고리즘
# 카프-라빈 알고리즘
# KMP 알고리즘
# 보이어-무어 알고리즘

# 고지식한 알고리즘 (Brute Force)
# 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의
# 문자들을 일일이 비교하는 방식으로 동작

t = 'TTTTTATTAATA'
p = 'TTA'

def Brute_Force(p,t):
    N = len(t)
    M = len(p)
    i = j = 0
    while i < N and j < M:
        if t[i] != p[j]:        # 다르면
            i = i - j + 1       # i - j 비교를 시작했던 위치
            j = 0
        else:
            i += 1
            j += 1
    if j == M:
        return i - j
    else:
        return -1

def pattern_count(p,t):     # 패턴의 등장 횟수 리턴
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:
            i += 1
            j += 1
        if j == M:
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt

# KMP 알고리즘
# 불일치가 발생한 텍스트의 앞 부분에 어떤 문자가 있는지를 알고 있으므로,
# 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
# 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함

# 보이어-무어 알고리즘
# 오른쪽에서 왼쪽으로 비교
# 점프를 뛰는 매커니즘
# 고려해야할 사항이 KMP 알고리즘보다 조금 더 있음

p = 'TTA'
t = 'TTTTTATTAATA'
N = len(t)
M = len(p)

def search(p,t):
    for i in range(N - M + 1):  # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(M):  # p에서 비교할 위치 인덱스
            if t[i + j] != p[j]:
                break
        else:  # break에 걸리지 않고 for가 끝난 경우 실행
            return i    # 패턴이 처음 나타난 인덱스 리턴
    return -1

print(search(p,t))
