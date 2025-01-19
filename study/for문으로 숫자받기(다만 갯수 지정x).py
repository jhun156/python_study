list = []
result = 0
for num in input().split():
    list.append(int(num))

for i in list:
    result += i

print(result)