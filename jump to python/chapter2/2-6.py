# s1 = set([1,2,3])
# l1 = list(s1)
# print(l1[0])

# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# print(s1 & s2)
# print(s1.intersection(s2))
# print(s1 | s2)
# print(s1.union(s2))
# print(s1 - s2)
# print(s1.difference(s2))

# s1 = set([1,2,3])
# s1.add(4)
# print(s1)

# s1 = set([1,2,3])
# s1.update([4,5,6])
# print(s1)

# s1 = set([1,2,3])
# s1.remove(2)
# print(s1)

# l1 = [1,1,1,2,2,2,2,2,3,3,3,4,]
# l1 = list(set(l1))
# print(l1)

# a = 1 == 1
# print(a)

# a = 1 < 2
# print(a)

# a = [1, 2, 3]
# b = a[:] #slicing
# a[1] = 4 
# print(a)
# print(b)

# a, b = 1, 2
# print(a)
# print(b)

# a = b = 'python'
# print(a + b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)