list = []

for i in map(int,input().split()):
    list.append(i)

a = int(input())

for i in range(3):
    list.append(a+i)

print(*list)