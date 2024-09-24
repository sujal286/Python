def count_word(str):
    words = str.split()  # Split the string into words based on whitespace
    return len(words)

s = count_word("sujal")
print("Number of words in sentence:", s)
