class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country

class F14(Jets):
    
    def __init__(self):
        self.name = "F14"
        self.origin = "USA"
        self.engine = 2
        self.seat = 2
        self.tail = 2
        self.speed = None
a = F14()

print(a.engine)
print(a.seat)
print(a.tail)
print(a.origin)
