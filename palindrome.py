num=int(input("enter the number:"))
rev=0
q=num
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10
if q==rev:
    print("it is palindrome number")
else:
    print("it is not palindrome")