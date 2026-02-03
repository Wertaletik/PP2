print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False


print(bool("Hello")) #True
print(bool(15)) #True


bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True


bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({})  #False


class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) #False


x = 200
print(isinstance(x, int)) #True