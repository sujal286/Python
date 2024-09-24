def duplicates(str):
    str=str.replace(" ", "")
    seen=set()
    for char in str:
        if char not in seen:
            seen.add(char)
    return seen

s=duplicates("sujal saha")
print("After removing duplicates character from string:",s)
