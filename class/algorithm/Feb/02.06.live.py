# 카운팅 정렬 (Counting Sort)
# 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여,
# 선형 시간에 정렬하는 효율적인 알고리즘
'''
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
'''
# ex) {1,2,3}을 포함하는 모든 순열을 생성하는 함수
# 순열의 요소 r개라면 r중 for문
'''
arr = [2, 3, 7]
for i1 in range(3):
    for i2 in range(3):
        if i2 != i1:
            for i3 in range(3):
                if i1 != i3 and i2 != i3:
                    print(arr[i1], arr[i2], arr[i3])
'''
# Baby-gin problem
# run : 연속된 3개 숫자, triplet : 같은 숫자 3개
# run, triplet으로만 구성된 숫자일때 정답
'''
data = list('444345')
counts = [0] * 10
for i in range(6):
    counts[int(data[i])] += 1
'''
# Baby-gin 반례 333456 (run을 먼저 확인하는 경우)
'''
# num = 456789
num = int(input())
c = [0] * 12
for _ in range(6):              # 단순 반복 6회
    c[num % 10] += 1            # 1의 자리를 알아내는 연산
    num //= 10                  # 1의 자리를 제거하는 연산
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2:
    print("Baby-Gin")
else:
    print("lose")
'''

