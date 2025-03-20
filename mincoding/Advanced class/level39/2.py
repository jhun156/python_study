coins = [10, 50, 100, 500]
coins.sort(reverse=True)
Min = 21e8
price = int(input())

def dfs(level,Sum):

    global Min
    if level > Min or Sum < 0:
        return

    if Sum == 0:
        Min = min(Min,level)

    for i in range(4):
        dfs(level+1,Sum-coins[i])


dfs(0,price)
print(Min)