import heapq
n = int(input())
left_heap = []
right_heap = []
heapq.heappush(left_heap, -500)
for _ in range(n):
    a, b = map(int,input().split())
    if a <= -left_heap[0]:
        heapq.heappush(left_heap, -a)
    else:
        heapq.heappush(right_heap, a)
    if b <= -left_heap[0]:
        heapq.heappush(left_heap, -b)
    else:
        heapq.heappush(right_heap, b)
    while len(left_heap) > len(right_heap) + 1:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
    while len(left_heap) < len(right_heap):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))
    print(-left_heap[0])