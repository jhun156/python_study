# 내 풀이

my_list = [i for i in input().split()]
count = 5

for i in my_list:
    if (ord(i) >= ord('A') and ord(i) <= ord("Z")) or (ord(i) >= ord('a') and ord(i) <= ord('z')):
        count -= 1

if count == 0:
    print("숫자미발견")
else:
    print(f"숫자{count}개발견")

# gpt 풀이 and 내 수정

def main():
    my_list = input().split()

    count = 0

    for i in my_list:
        if i.isdigit():
            count += 1
    
    if count == 0:
        print("숫자미발견")
    else:
        print(f"숫자{count}개발견")

main()