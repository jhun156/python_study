N = 6
arr = list(map(int,input().split()))
k = int(input())

# 자신의 차례때 먹거나 안먹거나
# 안먹으면 먹이가 2배가 되는 대신 못먹는 경우라면 공짜로 생기는 숫자를 놓침
# BFS DFS