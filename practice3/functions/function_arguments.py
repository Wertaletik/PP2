def my_function(name):
  print(name + " is here")
my_function("Tomas")
my_function("Werty")
my_function("Me")


def my_function(name):
  print("Hello", name)
my_function("Werty")


def my_function(name = "friend"):
  print("Hello", name)
my_function("Werty")
my_function("Qwerty")
my_function()


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "parrot", name = "Werty")