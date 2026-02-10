class aa:
    x = 5
bb = aa()
print(bb.x)

class phone:
    brand = "iphone"
    year = 2026
c = phone()
print(c.brand, c.year)

class Empty:
    pass
e = Empty()
print(type(e))

class game:
    boss = "666 HP"
class werty:
    collection = game()
v = werty()
print(v.collection.boss)

class group:
    students = ["Werty", "Niaven", "Goose"]
sg = group()
print(*sg.students)