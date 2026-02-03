fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#apple
#banana
#cherry


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    continue
#apple
#banana
#cherry


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#apple
#cherry