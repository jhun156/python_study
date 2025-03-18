import heapq
N = int(input())
arr = list(map(int,input().split()))

def ugly_number(n):
    heap = []
    heapq.heappush(heap,1)
    used = set([1])
    ugly_lst = []

    for _ in range(n):
        num = heapq.heappop(heap)
        ugly_lst.append(num)

        for i in [2,3,5]:
            new = num * i
            if new not in used:
                heapq.heappush(heap,new)
                used.add(new)

    return ugly_lst

for i in range(N):
    ans = ugly_number(arr[i])
    print(ans[-1], end=' ')