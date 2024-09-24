def pattern():
    r=int(input("Enter a number of rows:"))
    for i in range(r):
        for j in range(i):
            print("*",end="")
        print("\n")
pattern()
