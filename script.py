list = [i for i in map(int,input().split())]
sum = 0

for i in list:
    sum += i

aver = sum // 4

for i in list:
    if i > aver:
        print(f"{i}>{aver}")
    elif i < aver:
        print(f"{i}<{aver}")
    else:
        print(f"{i}=={aver}")

