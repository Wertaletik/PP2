x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


x = 5
y = "John"
print(type(x))
print(type(y)) 


x = "John"
# is the same as
x = 'John'


a = 4
A = "Sally"
#A will not overwrite a 


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


"""
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
"""


x, y, z = "Orange", "Banana", "Cherry"
print(x) #Orange
print(y) #Banana
print(z) #Cherry


x = y = z = "Orange"
print(x) #Orange
print(y) #Orange
print(z) #Orange


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) #apple
print(y) #banana
print(z) #cherry


x = "Python is awesome"
print(x) #Python is awesome


x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #Python is awesome


x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #Python is awesome


x = 5
y = 10
print(x + y) #15


"""
Error will occur
x = 5
y = "John"
print(x + y)
"""


x = 5
y = "John"
print(x, y) #5 John


x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc() #Python is awesome


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x) #Python is fantastic
myfunc()
print("Python is " + x) #Python is awesome


def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) #Python is fantastic


x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) #Python is fantastic


