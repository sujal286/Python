str=input("Enter string:")
def lengthop(st):
    count=0
    for i in st:
        count+=1
    print("Length of string is:",count)

    print(f"{count:>{count}} {st}")

lengthop(str)