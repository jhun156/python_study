# stack (Last In First Out, LIFO)
st=list()
st.append(2)
st.append(3)
st.append(4)
st.append(5)    # st = [2,3,4,5]

test = st.pop()
st.pop()
print(st)       # [2,3]

# stack은 append, pop 으로 쉽게 구현 가능

# Queue (First In First Out, FIFO)
q=list()
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)         # [3,4,5,6,7]
q.pop(0)            # O = 1
test = q.pop(0)     # pop(0), O = n
print(q)            # [5,6,7]

from collections import deque
q = deque()
q.append(5)
q.append(15)
q.append(25)
q.append(35)
q.append(45)
print(q)        # deque([5, 15, 25, 35, 45])
print(list(q))  # [5, 15, 25, 35, 45]

q.popleft()
q.popleft()
print(list(q))  # [25, 35, 45]

import queue        # 잘 안씀. 참고용
q = queue.Queue()
q.put(5)
q.put(15)
q.put(25)   # 추가할 땐 put
q.get()     # 제거할 땐 get
print(q)
print(q.queue)

# DFS

# 트리구조
# 1. 부모 관계, 2. 단방향
# 사이클 발생 X
# 맨 위의 노드를 root node
# 가장 아래 노드를 leaf node

# 트리 구조를 소스코드로 옮기는 방법
# 1. 인접 행렬, 2. 인접 리스트 3. 1차원 리스트 (이진 트리의 경우)

# 1. 인접 행렬
# 010010
# 001100 방식

# 2. 인접 리스트
# [[1,4]
#  [2,3]] 방식

name = 'ABCDEF'
arr = [
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

def dfs(now):
    print(name[now],end=' ')
    for x in range(6):
        if arr[now][x] == 1:
            dfs(x)

dfs(0)














