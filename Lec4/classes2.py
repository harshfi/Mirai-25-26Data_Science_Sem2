class Student:
    tenth=90 # class variable
    def __init__(self,name):
        self.name=name # instance variable
    
    def info(self):
        print(f"name={self.name}")
        

s1=Student("boss")
s1.info()