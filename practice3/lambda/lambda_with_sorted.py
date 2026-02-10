words = ["The", "World", "Is", "Yours"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words) 

nums = [-10, 5, -3, 2, -1]
sorted_abs = sorted(nums, key=lambda x: abs(x))
print(sorted_abs)  

pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda p: p[1])
print(sorted_pairs) 

names = ["Bayern", "Vitality", "Ruchka", "Alim"]
sorted_names = sorted(names, key=lambda n: n[-1])
print(sorted_names)  

scores = {"Magnus": 90, "Hikaru": 75}
sorted_scores = sorted(scores.items(), key=lambda item: item[1])
print(sorted_scores)