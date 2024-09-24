def Anagram_str(str1,str2):
    str1_length=len(str1)
    str2_length=len(str2)
    if str1_length!=str2_length:
        return False
    else:
        for char in str1:
            if char not in str2:
                return False
        return True

isAnagram=Anagram_str("sujal","lajusw")

if isAnagram:
    print("string is anagram")
else:
    print("string is not anagram")
