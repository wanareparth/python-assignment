class box:
    def __init__(self,weight):
        self.weight=weight
    def __add__(self, other):
        return self.weight+other.weight
b1=box(659)
b2=box(353)
print(b1+b2)

#method overloding
class calc:
    def add(self,a,b=0,c=0):
        return a+b+c
    
c=calc()
print(c.add(10))
print(c.add(10,20))
print(c.add(10,20,30))

#overriding
class vehical:
    def move(self):
        print("vehicle is moving")
class car(vehical):
    def move(self):
        print("vehicle is driving")
class cycle(vehical):
    def move(self):
        print("pedalling on road")
c0=vehical()        
c=car()
c1=cycle()
c0.move()
c.move()
c1.move()
