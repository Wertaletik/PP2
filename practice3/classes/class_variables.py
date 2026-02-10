class Box:
    v = 5

p = Box()
q = Box()
print(p.v, q.v)



class Tally:
    n = 0

Tally.n += 1
print(Tally.n)



class Human:
    kind = "Human"

    def __init__(self, n):
        self.n = n

h = Human("Werty")
print(h.n, h.kind)



class Disk:
    k = 3.14

    def __init__(self, r):
        self.r = r

    def calc(self):
        return Disk.k * self.r * self.r

d = Disk(2)
print(d.calc())



class Team:
    lst = []

Team.lst.append("A")
Team.lst.append("B")
print(Team.lst)
