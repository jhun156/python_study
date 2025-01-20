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