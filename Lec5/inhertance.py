class parent:

    def properties(self):
        return "car banglow 100 cr"
    
    def marks(self):
        return "90 %"
    
    def nature(self):
        return "good in nature"
    


class child(parent):
     
    #  @override
    def marks(self):
        return "60 %"
    
    def nature (self):
        return "bekar"
    

# class grandChild(child):
    

c1=child()

print(c1.properties())

    

    

