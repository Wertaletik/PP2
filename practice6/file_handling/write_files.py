with open("./practice6/sample.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("This is Python.\n")

with open("./practice6/sample.txt", "a") as f:
    f.write("Appending a third line.\n")