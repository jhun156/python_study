# import sys
# sys.stdin = open("input.txt","r")
import heapq

# heapq와 MST 알고리즘을 병합해 풀이했습니다.

def find(n):                # 같은 부모인지 확인하는 함수
    if parent[n] == n:
        return n

    ret = find(parent[n])
    parent[n] = ret
    return ret

T = int(input())
for tc in range(1,T+1):         # 입력받기
    N = int(input())
    arr = [[0,0]]
    for _ in range(N):
        tmp = list(map(int,input().split()))
        arr.append(tmp)

    heap = []
    for i in range(N+1):
        for j in range(i+1,N+1):
            distance = abs(arr[i][0]-arr[j][0]) + abs(arr[i][1]-arr[j][1])  # 서로 다른 점끼리의 길이
            heapq.heappush(heap, (distance, i, j))          # 적은 길이 순서로 heap에 정렬되도록 distance 값 추가해서 넣어줌
                                                            # heap 에서 MST 알고리즘의 원리와 동일하게 최소 길이 먼저 확인함
    parent = [i for i in range(N+1)]                        # 같은 부모인지 확인하기 위한 배열
    ans = 0

    while heap:
        distance, nextx, nexty = heapq.heappop(heap)
        A = find(nextx)
        B = find(nexty)
        if A == B:
            continue            # 만약 같은 부모라면 넘어감

        parent[A] = B           # 부모가 같지 않다면 길이를 추가하고 같은 부모로 변경
        ans += distance

    print(f"#{tc} {ans}")
