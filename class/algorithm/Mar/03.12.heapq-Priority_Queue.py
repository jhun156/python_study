# from queue import PriorityQueue - 알고리즘 분야에서 안씀
import heapq    # 기본값은 Min heap 이며 Max heap은 기능 없음

# heappush
# heap의 규칙에 의거해서 arr에 넣는다는 뜻
# 디버깅할때 루트노드에 우선순위가 가장 높은 값이 들어있는지 확인하면 됨

# arr = []
# heapq.heappush(arr,4)
# heapq.heappush(arr,6)
# heapq.heappush(arr,1)
# heapq.heappush(arr,2)
# heapq.heappush(arr,3)
# heapq.heappush(추가하고싶은 리스트, 원소값)

# heappop
# heap의 규칙에 의거해서 arr에서 pop 하는 것

# for i in range(len(arr)):
#     print(heapq.heappop(arr))       # N log N
# heapq.heappop(pop하고자 하는 리스트)

# while arr:
#     tmp = heapq.heappop(arr)
#     print(tmp,end=' ')      # while문을 사용해서 pop하는 경우 이런식으로 사용

# heapq.heapify(heapq로 만들고 싶은 리스트)
# 이미 원소가 있는 리스트를 heap 규칙에 맞게 한번에 변환하는 방법

# arr = [3422,5,3,1,5]
# heapq.heapify(arr)
# print(arr)

# Max heap

arr = [3422,5,3,1,5]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap,-arr[i])        # Max heap 순서로 집어넣는 방법, 대신 음수로 들어가므로 추가 조작 필요함

for i in range(len(arr)):
    print(-heapq.heappop(heap))         # Max heap 순서로 pop, 음수이므로 - 붙여줌. 표현법 중요

arr = [3422,5,3,1,5]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap,(-arr[i],arr[i]))       # Max heap 순서로 push 하는 방법 2번째.
print(heap)

for i in range(len(arr)):
    print(heapq.heappop(heap)[1],end=' ')
print()                                         # Max heap 순서로 pop하고 출력

arr = [3422,5,3,1,5]
heap=list(map(lambda x:-x,arr))
heapq.heapify(heap)
for i in range(len(arr)):
    print(-heapq.heappop(heap),end=' ')         # heapify를 이용한 방법
print()


