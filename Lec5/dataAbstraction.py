class bank:
    # __tax=0.001
    def __init__(self, name,balance):
        self.name="harsh"
        self.__bal=balance  #__ -> private
    
    def deposit(self,amt):
        self.__bal=self.__bal+tax(amt)

    def checkBal(self):
        return self.__bal
    
    def __tax(self,amt):
        return 0.99*amt
    
