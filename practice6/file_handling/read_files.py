with open(r"C:\Study\PP2\practice6\sample.txt", "r") as f:
    a = f.readline()
    b = f.readline()
    print(a, end="")
    print(b, end="")

    # c = f.read()
    c = f.readlines()
    print(" ".join(i.strip("\n") for i in c))
