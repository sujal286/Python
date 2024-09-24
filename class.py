class A:
    name="Sujal Saha"
    roll=45
    def __init__(self):
        print("Hello Sujal")

    def welcome(self):
        print("Welcome,",self.name)

obj=A()
print(obj.name)
print(obj.roll)
obj.welcome()

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average_marks(self):
        sum=0
        for val in self.marks:
            sum+=val

        print("Average marks:",sum/3)

ob=Student("Sujal Saha",[89,95,78])
ob.average_marks()

