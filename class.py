class Category:
    def __init__(self,category,amount):
        self.category = category
        self.amount = amount
    def deposit(self):
        print("This is deposit function")
        pass
    def withdraw(self):
        pass
    def transfer(self):
        pass
    def checkBalance(self):
        pass

category1 = Category("food",100)
category2 = Category("clothing",250)
category3 = Category("carExpenses",200)
category4 = Category("entertainment",150)

category1.deposit()