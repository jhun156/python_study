# 내 풀이

a, b, c = input().split()
flag = 0

def process():
    global a,b,c,flag
    if ord(a) == ord("A") and ord(b) == ord("B") and ord(c) == ord("C"):
        flag = 1

def output():
    global flag
    if flag == 1:
        print("ABC를찾았다")
    else:
        print("못찾았다")

def main():
    process()
    output()

main()

# gpt 풀이

def main():
    a, b, c = input().split()
    if a == "A" and b == "B" and c == "C":
        print("ABC를찾았다")
    else:
        print("못찾았다")

main()