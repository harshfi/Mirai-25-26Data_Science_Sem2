class bank:
    def __init__(self, name,balance):
        self.name="harsh"
        self.__bal=balance  #__ -> private
    
    def deposit(self,amt):
        self.__bal=self.__bal+amt

    def checkBal(self):
        return self.__bal

    

p1= bank("harsh",50)

print(p1.name)
p1.name="tripathi"

# print(p1.checkBal())

p1.deposit(100)

print(p1.checkBal())