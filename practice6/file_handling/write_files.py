with open("sample.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("This is Python.\n")

with open("sample.txt", "a") as f:
    f.write("Appending a third line.\n")