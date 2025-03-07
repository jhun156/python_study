# import sys
# sys.stdin = open("input.txt","r")

def dfs(num):

    global cnt
    if not lst[num]:
        return

    for i in lst[num]:
        cnt += 1
        dfs(i)

T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split())
    # 간선의 개수, 노드 N (root)
    lst = [[] for _ in range(1002)]
    location = list(map(int,input().split()))
    for i in range(0,2*E,2):
        lst[location[i]].append(location[i+1])
    # 인접 리스트 생성
    cnt = 1
    dfs(N)  # N번 노드로 탐색 시작
    print(f"#{tc} {cnt}")