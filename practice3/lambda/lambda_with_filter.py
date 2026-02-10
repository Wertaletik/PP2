nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(*evens)  

words = ["Hello", "Peaceful", "Beautiful", "World"]
short_words = list(filter(lambda w: len(w) < 6, words))
print(*short_words)  

nums = [-2, -1, 0, 1, 2]
positives = list(filter(lambda x: x > 0, nums))
print(*positives)  

names = ["Dima", "Zheks", "Muha", "Miko"]
b_names = list(filter(lambda n: n.startswith("B"), names))
print(*b_names)  

nums = [3, 6, 7, 9, 10, 12]
div_by_three = list(filter(lambda x: x % 3 == 0, nums))
print(*div_by_three)

nums = [1, 2, 3, 4, 5, 6]
plus_even = list(map(lambda x: x + 2, filter(lambda x: x % 2 == 0, nums)))
print(*plus_even)