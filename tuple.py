a=(1,2,3)
b=(4,5,6)
print(a+b)
print(a[1])
print(a.count(2))
if 4 in a:
    print("it contains 4")
else:
    print("it not contains 4")
string=str(a)
print(string)
list=[1,2,3,4,5,6]
tup=tuple(list)
print(tup)

for i in a:
    if i in b:
        print("true")
