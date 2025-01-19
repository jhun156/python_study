my_list = []

def custom_input():
    global my_list
    for i in map(int,input().split()):
        my_list.append(i)

def output():
    global my_list
    my_list.reverse()
    for i in my_list:
        print(i,end='')

def main():
    custom_input()
    output()

main()