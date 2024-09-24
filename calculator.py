a=input("enter the number:")
b=input("enter the operator:")
c=input("enter the second number:")
a=int(a)
c=int(c)
if b=="+":
    print((a)+(c))
elif b=="-":
    print((a)-(c))
elif b=="*":
    print((a)*(c))
elif b=="%":
    print((a)%(c))
else:
    print((a)/(c))