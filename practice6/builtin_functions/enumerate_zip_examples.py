names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]


for index, name in enumerate(names, 1):
    print(f"{index}: {name}")


for i in zip(names, scores):
    print(f"{i[0]} scored {i[1]}")