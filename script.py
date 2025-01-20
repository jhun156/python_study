arr = [i for i in map(int,input().split())]
number = 1

for i in arr:
    if i >= 70:
        print(f"{number}번사람은{i}점PASS")
        number += 1
    elif i >= 50:
        print(f"{number}번사람은{i}점RETEST")
        number += 1
    else:
        print(f"{number}번사람은{i}점FAIL")
        number += 1

