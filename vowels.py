def vowels(str):
    vowel={"a","e","i","o","u"}
    for i in str:
        if i in vowel:
            return True
    return False
found_vowel=vowels("pplm")
if found_vowel:
    print("it contains vowels")
else:
    print("it does not contain any vowels")




