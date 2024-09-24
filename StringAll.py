#String is immutable in python (value cannot be change)
str1="sujal"
str2=" Saha"
str3=str1+str2
#concatenate
print(str1+str2)
#length of string
print(len(str1))
print(len(str2))
#indexing
print(str1[2])
#slicing
print(str3[0:5])
print(str3[::-1]) #reverse
print(str3[-4:])
#string function
print(str3.endswith("ha"))
print(str3.capitalize())
print(str3.replace("sujal","Shilpa"))
print(str3.find("sujal"))
print(str3.count("a"))
print(str3.split())
