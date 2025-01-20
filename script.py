<<<<<<< HEAD
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

=======
my_list = []

def custom_input():
    global my_list
    a = input()
    my_list = [[a for i in range(4)] for j in range(4)]

def output():
    global my_list
    for i in my_list:
        for j in i:
            print(j,end='')
        print()

custom_input()
output()
>>>>>>> 7585950dd32b533864027730c614bcf92f6fa236
