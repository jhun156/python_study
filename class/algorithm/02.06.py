# 카운팅 정렬 (Counting Sort)
# 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여,
# 선형 시간에 정렬하는 효율적인 알고리즘

data = [0, 4, 1, 3, 1, 2, 4, 1]
n = len(data)
counts = [0] * (max(data)+1)
temp = [0] * n
for i in range(n):
    counts[data[i]] += 1
for i in range(1,max(data)+1):                # counts[i]까지의 합계
    counts[i] += counts[i-1]
for i in range(len(data)-1,-1,-1):
    counts[data[i]] -= 1            # data[i]까지의 개수 1개 감소
    temp[counts[data[i]]] = data[i]
    # data[i]까지 차지한 칸 수 중 가장 오른쪽에 data[i] 기록

print(temp)