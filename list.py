#list are mutable its value can be change
marks =[ 99, 21, 90, 85]
print(len(marks))
#slicing
print(marks[1:3])
marks.append(98)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks[1:2] =[56]
print(marks)
marks.insert(2,78)
print(marks)
marks.remove(78)
print(marks)
marks.pop(2)
print(marks)
m=marks.copy()
print(m)
