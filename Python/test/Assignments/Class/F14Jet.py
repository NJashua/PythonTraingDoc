class Jets:
    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country    
class F14(Jets):
    def __init__(self):
        super().__init__(name="F14", country="USA")
a=F14() 
print(a.origin)
print(a.name)
