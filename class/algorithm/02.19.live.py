# 큐 생성
queue = [0] * 3
front = rear = -1   # 큐 생성단계

# 선형큐
# 1,2,3 인큐
rear += 1
queue[rear] = 1     # enQueue1

rear += 1
queue[rear] = 2     # enQueue2

rear += 1
queue[rear] = 3     # enQueue3

while front != rear:
    front += 1
    t = queue[front]
    print(t)
