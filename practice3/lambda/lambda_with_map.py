nums = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x**3, nums))
print(*cubes)  

words = ["HeLlO", "WoRlD"]
lower_words = list(map(lambda w: w.lower(), words))
print(*lower_words)  

nums = [1, 2, 3]
plus = list(map(lambda x: x + 10, nums))
print(*plus)  

words = ["Hello", "World"]
lengths = list(map(lambda w: len(w), words))
print(*lengths)  

nums = [2, 4, 6]
doubled = list(map(lambda x: x * 2, nums))
print(*doubled)