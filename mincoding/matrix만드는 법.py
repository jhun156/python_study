# 1번 방법

arr = [["a" for i in range(4)] for j in range(4)]

print(*arr)


# 2번 방법

matrix = []

for i in range(4):
    row = ["a"] * 4
    matrix.append(row)

print(*matrix)

# 3번 방법

matrix = []

for i in range(4):
    num = ["a"] * 4
    matrix.append(num)

print(*matrix)