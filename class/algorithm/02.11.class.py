def abc(level):
    global cnt

    if level==3:
        return

    for i in range(3):
        cnt += 1
        abc(level+1)
        cnt += 1
cnt = 0
abc(0)
print(cnt)