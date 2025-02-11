def abc(level):
    print("1")
    global cnt

    if level==2:
        return

    for i in range(2):
        abc(level+1)

cnt = 0
abc(0)
print(cnt)