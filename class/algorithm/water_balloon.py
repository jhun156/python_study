lst=[
['_','_','_','_','B','_','_',],
['_','_','_','_','_','_','_',],
['_','A','A','_','_','_','_',],
['_','_','_','_','_','_','_',],
['_','_','A','_','_','_','_',],
['_','#','#','_','B','_','_',],
['_','_','_','_','#','_','_',]]

# 7*7 배열
# A는 5칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# B는 3칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# '#'은 벽이다
# 벽 그리고 A,B 뒤로는 물풍선이 터지지 않는다.

# 물을 피할곳은 지도상 몇군데인가? - 16 -

def bomb(y,x,num):
    lst[y][x] = "@"
    directY = [0,0,1,-1]
    directX = [1,-1,0,0]
    for i in range(4):
        for j in range(1,num+1):
            dy = y + directY[i] * j
            dx = x + directX[i] * j
            if dy < 0 or dy > 6 or dx < 0 or dx > 6:
                continue
            if lst[dy][dx] == 'A' or lst[dy][dx] == 'B' or lst[dy][dx] == '#':
                break
            else:
                lst[dy][dx] = '@'

for i in range(7):
    for j in range(7):
        if lst[i][j] == 'A':
            bomb(i,j,5)
        elif lst[i][j] == 'B':
            bomb(i,j,3)

ans = 0
for i in range(7):
    for j in range(7):
       if lst[i][j] == '_':
           ans += 1

print(ans)













