my_list = []

a, b = map(int,input().split())

my_list.extend(a + i for i in range(3))
my_list.extend(int(b) - 2 + int(i) for i in range(3))

for i in my_list:
    print(i,end = ' ')