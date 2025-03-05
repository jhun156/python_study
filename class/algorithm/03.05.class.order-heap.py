arr =" ABCDEFG"

# 전위순회 ABDECFG

def preorder(now):

    if now > len(arr)-1:
        return
    print(arr[now],end=' ')
    preorder(now*2)
    preorder(now*2+1)

preorder(1)

print()

# 후위순회 DEBFGCA

def postorder(now):

    if now > len(arr) - 1:
        return
    postorder(now * 2)
    postorder(now * 2 + 1)
    print(arr[now], end=' ')

postorder(1)

print()

# 중위순회 DBEAFCG

def inorder(now):

    if now > len(arr) - 1:
        return
    inorder(now * 2)
    print(arr[now], end=' ')
    inorder(now * 2 + 1)

inorder(1)

print()

# BST : Binary Search Tree
# balanced tree
    # red-black tree
    # B - tree

# 구현
# 1. 입력된 데이터를 트리 구조로 저장
# 2. 입력된 값 찾기

arr = [0] * 20 # 트리의 형태로 저장할 1차원 배열 만들기
lst = [4,2,9,7,15,1]

def insert(value):
    now = 1 # 내가 저장할 인덱스
    while 1:
        if arr[now] == 0:
            arr[now] = value
            return
        elif arr[now] < value:
            now = now*2 + 1
        else:
            now = now*2

for i in lst:
    insert(i)

n = int(input())

def search(target):
    now = 1
    while 1:
        if now >= 20:
            return 0
        elif arr[now] == target:
            return 1
        elif arr[now] < target:
            now = now*2 + 1
        else:
            now = now*2

ans = search(n)

if ans:
    print("있음")
else:
    print("없음")

# heap : '우선순위'가 가장 높은 것을 우선으로 출력 ( N log N )

arr = [6,4,1,4,7,8,1]
heap = [0] * 20
hindex = 1

# insert 함수 완전이진트리로 저장
# top() 루트노드를 리턴하는 함수
# pop() 루트노드 출력 후 맨 뒤의 값을 맨 앞으로 올리고 자식들과 비교 후 스왑

def insert(value):

    global hindex
    heap[hindex] = value    # 루트노드 저장
    now = hindex
    hindex += 1
    while 1:
        p = now // 2    # 부모인덱스 구하기
        if p == 0:
            break       # 해당 노드가 루트노드라면 off
        if heap[p] > heap[now]:
            break       # 부모가 크거나 같으면 off (Max heap)
        heap[now],heap[p] = heap[p],heap[now]   # 부모가 더 작으면 자식과 스왑
        now = p         # while문 반복

def top():
    return heap[1]

def pop():
    global hindex
    hindex -= 1
    heap[1] = heap[hindex]
    heap[hindex] = 0
    now = 1
    while 1:
        son = now * 2
        rson = son + 1
        if rson < hindex and heap[son] < heap[rson]:
            son=rson
        if son >= hindex and heap[now]>heap[son]:
            break
        heap[now],heap[son] = heap[son],heap[now]
        now=son

for i in range(len(arr)):
    insert(i)

for i in range(len(arr)):
    print(top(),end=' ')
    pop()


