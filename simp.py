def Prime_number(n):
    isPrime=True
    for i in range(2,n):
        if(n%i==0):
            isPrime=False
            break
    if(isPrime):
        print(n," is a prime number")
    else:
        print("it is not prime")
Prime_number(46)