n=eval(input("Enter a number:"))
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
        break
if prime:
    print("the number is prime")
else:
    print("the number is not prime")