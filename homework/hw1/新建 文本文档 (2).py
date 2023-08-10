import operator

class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return self.opStr + '(' + \
               str(self.left) + ', ' +\
               str(self.right) + ')'
    __repr__ = __str__
    
class Sum(BinaryOp):
    opStr = 'Sum'
    def eval(self,env):
        return(operator.add(self.left.eval(env),self.right.eval(env)))

class Prod(BinaryOp):
    opStr = 'Prod'
    def eval(self,env):
        return(operator.mul(self.left.eval(env),self.right.eval(env)))    
class Quot(BinaryOp):
    opStr = 'Quot'
    def eval(self,env):
        return(operator.truediv(self.left.eval(env),self.right.eval(env)))
class Diff(BinaryOp):
    opStr = 'Diff'
    def eval(self,env):
        return(operator.sub(self.left.eval(env),self.right.eval(env)))
class Assign(BinaryOp):
    opStr = 'Assign'
    def eval(self,env):
        env[self.left.name]= self.right.eval(env)
        return self.right.eval(env)
class Number:
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return 'Num('+str(self.value)+')'
    __repr__ = __str__
    def eval(self):
        return float(self.value)
class Variable:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Var('+self.name+')'
    __repr__ = __str__
    def eval(self,env):
        return(env.get(self.name))


def testEval():
    env = {}
    Assign(Variable('a'), Number(5.0)).eval(env)
    print (Variable('a').eval(env))
    env['b'] = 2.0
    print (Variable('b').eval(env))
    env['c'] = 4.0
    print (Variable('c').eval(env))
    print (Sum(Variable('a'), Variable('b')).eval(env))
    print (Sum(Diff(Variable('a'), Variable('c')), Variable('b')).eval(env))
    Assign(Variable('a'), Sum(Variable('a'), Variable('b'))).eval(env)
    print (Variable('a').eval(env))
    print (env)


testEval()




