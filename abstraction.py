class Account:
    balance=50000
    acc=18903393032

    def debit(self,amount):
        self.balance-=amount


    def credit(self,amount):
        self.balance+=amount

    def bal(self):
        print("Balance:",self.balance)

obj=Account()
print("balance:",obj.balance)
print("After debit or credit:")
#obj.debit(3000)
obj.credit(5000)
obj.bal()
