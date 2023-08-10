class V2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return'V2[{0},{1}]'.format(self.x,self.y) 
    def getX(self):
        print(self.x)
    def getY(self):
        print(self.y)
    def add(self,other):
        return V2(self.x+other.x,self.y+other.y)
    def mul(self,n):
         return V2(self.x*n,self.y*n)
    def __add__(self, v):
        return self.add(v)
    def __mul__(self,v):
        return self.mul(v)
p=V2(1,2)
o=V2(5,6)
print(p)
print(o)
p.getX()
p.getY()
print(p.add(o))
print(p.mul(2))
print(p+o)
print(p*3)
input("")







