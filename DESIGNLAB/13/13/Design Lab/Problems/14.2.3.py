import lib601.util as util

class MyClass:
    def __init__(self, v):
        self.v = v
#def lotsOfClass(n, v):
    #result = []
    #for i in range(n):
        #one = MyClass(v)
        #result.append(one) 
    #return result
def Class1(v):
    one = MyClass(v)
    return one
def lotsOfClass(n, v):
    result = util.makeVectorFill(n,lambda x:Class1(v))    
    return result
class10 = lotsOfClass(10,'oh')
class10[0].v = 'no'

