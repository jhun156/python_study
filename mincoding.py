a, b = map(int,input().split())

my_list = [a + i for i in range(0,int(b-a)+1)]

for i in my_list:
    print(i,end='')