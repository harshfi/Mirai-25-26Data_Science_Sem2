class student:
    name=""
    roll=0
    age=""
    def info(self):
        print(f"name={self.name} roll={self.roll} age={self.age}")


s1=student()

s1.name="boss"
s1.roll=1
s1.age=46
s1.info()

s2=student()

s2.name="babul"
s2.roll=420
s2.age=50

s2.info()