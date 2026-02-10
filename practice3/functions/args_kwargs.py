def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))

def list(**kwargs):
    c=[]
    for a,b in kwargs.items():
        c.append(f"{a}: {b}")
    return ', '.join(c)
print(list(x=1,y=2,z=3))