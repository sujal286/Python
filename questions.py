def unique(str):
    seen=set()
    for char in str:
        if(char in seen):
            return False,seen
        seen.add(char)
    return True,seen
is_unique, seen_chars = unique("sujal saha")
if is_unique:
    print("all characters are unique in this string:",seen_chars)
else:
    print("characters are not unique")

