class A:
    def __init__(self,name):
        self.name=name
        print("Name:",name)

class B(A):
    def __init__(self,roll):
        super().__init__("Sujal Saha")
        self.roll=roll
        print("Roll:",roll)

class C(B):
    def __init__(self):
        super().__init__(104)
        print("Details completed")

obj=C()

