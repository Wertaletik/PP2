from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


square = list(map(lambda x: x**2, list1))
print(square)

odd = list(filter(lambda x: x % 2 == 1, list1))
print(odd)


total = reduce(lambda x, y: x - y, list1)
print(total)

totalrev = reduce(lambda x, y: x - y, reversed(list1))
print(totalrev)