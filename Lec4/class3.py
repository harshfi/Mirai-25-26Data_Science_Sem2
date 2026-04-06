
class Phone:
    
    color="black"
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def isTouchScreen(self):
        return self.price>10000
    
p1=Phone("Apple","iPhone 15",50000)

p2=Phone("Nokia","3310",1500)

print(p1.isTouchScreen())
print(p2.isTouchScreen())
