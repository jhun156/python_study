import heapq

heap = []
# 인접 리스트
N,M = map(int,input().split())
arr = [[] for _ in range(N)]
for i in range(M):
    index,do,cost = map(int,input().split())
    arr[index].append((do,cost))
start,end = map(int,input().split())

heapq.heappush(heap,(0,start))
result = [21e8] * N
result[start] = 0

while heap:

    ky_cost,ky_index = heapq.heappop(heap)

    if ky_cost > result[ky_index]:
        continue

    for end,end_cost in arr[ky_index]:
        straight = result[end]
        curve = ky_cost+end_cost
        if curve < straight:
            result[end] = curve
            heapq.heappush(heap,(curve,end))

print(*result)
print(result[end])