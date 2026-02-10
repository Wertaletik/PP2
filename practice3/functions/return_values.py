def square(x):
    return x**2

def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder
w,e=divide(3,2)
print(w,e)

def format_name(first, last):
    return f"{last}, {first}"
print(format_name("Hello", "World"))

def is_even(n):
    return n % 2 == 0
if is_even(2):
    print("Werty")

def multiples(n, count):
    return [n * i for i in range(1, count + 1)]
print(*multiples(3,10))