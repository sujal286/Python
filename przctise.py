my_str="sujal is a good a boy"
print(my_str[-13:-3])
print(my_str[::-1])
count=0
for char in my_str:
    if "a"==char:
        count=count+1
print("number of a is:",count)
print(my_str.split())
print(my_str.lower())
print(my_str.upper())
print(my_str.capitalize())
print(my_str.count("s"))
print(my_str.title())

s=my_str.split()
reverse_s=s[::-1]
print(" ".join(reverse_s))

my_s=input("Enter a string:")
reversed_str=my_s[::-1]
if(my_s==reversed_str):
    print("string is palindrome")
else:
    print("string is not palindrome")