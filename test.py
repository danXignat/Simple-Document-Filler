class Base:
    def __init__(self):
        a = 1
        b = 2
        
        self.miau1()
        self.miau2()
        
    def miau1(self):
        print("miau1")
        
    def miau2(self):
        ...
        
class Derived(Base):
    def miau2(self):
        print("Derived miau2")
        
        
# test = Derived()
ls = []
ls.append(1, 2)