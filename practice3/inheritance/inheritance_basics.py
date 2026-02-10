class Being:
    def talk(self):
        print("Sound")

class Dog(Being):
    pass

a = Dog()
a.talk()

class Bird(Being):
    def move(self):
        print("Fly")

b = Bird()
b.talk()
b.move()



class Auto:
    a = 4
    n = 3

class Cycle(Auto):
    n = 2

print(Cycle().a)
print(Cycle().n)



class User:
    def hi(self):
        print("Hi")

class Learner(User):
    def study(self):
        print("Study")

c = Learner()
c.hi()
c.study()



class Base:
    def __init__(self, n):
        self.n = n

class Sub(Base):
    pass

d = Sub(5)
print(d.n)