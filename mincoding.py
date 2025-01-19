list = []
result = 0
for num in map(int,input().split()):
    list.append(num)

for i in list:
    result += i

print(result)