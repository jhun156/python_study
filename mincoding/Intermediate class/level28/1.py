lst = ['Amy','Bob','Chloe','Edger','Diane']
arr = [1,2,3,4,5]
test = [
    [2,1],
    [3,2],
    [5,2],
    [4,1],
]

empty = [0] * (5+1)
for i in range(4):
    empty[test[i][0]] += 1

a = empty.index(max(empty))
a -= 1
print(lst[a])