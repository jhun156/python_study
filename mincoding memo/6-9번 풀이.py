a = input()

my_list = [i for i in range(ord("A"),ord(a)+1)]

for i in my_list:
    print(chr(i), end = '')