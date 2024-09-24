class A:
    def get_xy(self,x,y):
        self.x=x
        self.y=y
    def show_xy(self):
        print("X=",self.x," Y=",self.y)

class B():
    def get_pq(self,p,q):
        self.p=p
        self.q=q
    def show_pq(self):
        print("P=",self.p," Q=",self.q)
class C(A,B):
    def __init__(self):
        print("Hello")

obj=C()
obj.get_xy(10,20)
obj.show_xy()
obj.get_pq(30,40)
obj.show_pq()