import heapq
N = int(input())
heap = []
for i in range(N):
    tmp = int(input())
    heapq.heappush(heap,tmp)

Sum = 0
while heap:

    if N >= 2:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        Sum += (a + b)
        heapq.heappush(heap,a+b)
        N -= 1

    else:
        break

print(Sum)