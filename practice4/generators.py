def square(wer):
    for i in wer:
        yield i**2

n = int(input())
for i in square(range(1,n+1)):
    print(i,end=" ")
print()



print("-"*100)
def even(wer):
    for i in wer:
        if i%2==0:
            yield i

n=int(input())
print(*list(i for i in even(range(n+1))),sep=", ")



print("-"*100)
def thrfour(wer):
    for i in wer:
        if i%12==0:
            yield i


n=int(input())
for i in thrfour(range(n+1)):
    print(i,end=" ")
print()



print("-"*100)
def squares(wer):
    for i in wer:
        yield i**2

a=int(input())
b=int(input())
print(*list(i for i in squares(range(a,b+1))),sep=", ")




print("-"*100)
def to0(wer):
    while wer>=0:
        yield wer
        wer-=1

n=int(input())
for i in to0(n):
    print(i)