class Card:
    balance = 0

    def __init__(self, bal):
        self.balance = bal
        self

    def withdraw(self,amount):
         if self.balance >= amount:
             self.balance -= amount + (0.2*amount)
             return self.printReceipt(self.balance,amount)
         else:
             return "insufficient balance"

    def printReceipt(self,balance,withdraw):
         return  """ AMOUNT :.....{}
                     BALANCE :.....{}
          """.format(withdraw,balance)