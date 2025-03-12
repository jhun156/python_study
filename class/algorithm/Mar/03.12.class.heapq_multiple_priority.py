arr = [(1,5),(1,9),(4,2)]
# 우선순위 조건
# 1. 첫번째 원소 내림차순
# 2. 두번째 원소 오름차순

import heapq
class Node:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __lt__(self, other):    # less than
        if self.a > other.a: return True
        if self.a < other.a: return False
        return self.b < other.b

heap=[]
heapq.heappush(heap,Node(1,5))
heapq.heappush(heap,Node(1,9))
heapq.heappush(heap,Node(4,2))

while heap:
    tmp = heapq.heappop(heap)
    print(tmp.a,tmp.b)

arr = [(1,5),(1,9),(4,2)]
heap = list(map(lambda x:Node(x[0],x[1]),arr))
heapq.heapify(heap)

while heap:
    tmp = heapq.heappop(heap)
    print(tmp.a,tmp.b)      # 이때 tmp.a, tmp.b 는 숫자가 아니고 문자임