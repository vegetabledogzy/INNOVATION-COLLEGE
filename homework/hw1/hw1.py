import pdb
import lib601.sm as sm
import string
import operator

class SM:
    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]
    
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
        return operator.add(self.left.eval(env),self.right.eval(env))
class Prod(BinaryOp):
    opStr = 'Prod'
    def eval(self,env):
        return operator.mul(self.left.eval(env),self.right.eval(env))
class Quot(BinaryOp):
    opStr = 'Quot'
    def eval(self,env):
        return operator.truediv(self.left.eval(env),self.right.eval(env))
class Diff(BinaryOp):
    opStr = 'Diff'
    def eval(self,env):
        return operator.sub(self.left.eval(env),self.right.eval(env))
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
    def eval(self,env):
        return self.value
class Variable:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Var('+self.name+')'
    __repr__ = __str__
    def eval(self,env):
       return env.get(self.name)

# characters that are single-character tokens
seps = ['(', ')', '+', '-', '*', '/', '=',' ']

# Convert strings into a list of tokens (strings)
def tokenize(string):
    list1=list(string)#��string���
    list2=['']*100#������Զ�Ԫ�ش���Ŀ��б�
    j=0
    for i in range(len(list1)):#�����б�
        if list1[i] in seps:#��list[i]�Ƿָ����ר����һ��һ��Ϊ�յ�list[j]����
            j=j+1
            list2[j]=str(list2[j])+str(list1[i])
            j=j+1
        if list1[i] not in seps:#list[i]���Ƿָ�������ڿ��ܲ�Ϊ�յ�list2[j]����
            list2[j]=str(list2[j])+str(list1[i])
    while '' in list2:
        list2.remove('')#ȥ���б�Ŀ�Ԫ��
    while ' ' in list2:
        list2.remove(' ')#ȥ���б�Ŀո�Ԫ��
    return list2
    pass

# tokens is a list of tokens
# returns a syntax tree:  an instance of {\tt Number}, {\tt Variable},
# or one of the subclasses of {\tt BinaryOp}
def parse(tokens):
    def parseExp(index):
        if numberTok(tokens[index]):#�ڳ������Ѿ�����ĺ�������ֵΪ����ֵ�����б�indexλ�����������������,����ת��ΪNumberʵ��������ʵ������һλ
           number=Number(float(tokens[index]))
           return (number,index+1)
        elif variableTok(tokens[index]):#�ڳ������Ѿ�����ĺ�������ֵΪ����ֵ�����б�����Ǳ���������,����ת��Ϊvariableʵ��������ʵ������һλ
            variable=Variable(str(tokens[index]))
            return (variable,index+1)#ͬʱ����ҲΪ�ݹ���õĽ�������
        else:#��������Ҳ���Ǳ��������������һ������ʶ��'(',��������һ��ݹ���� ex(index+1) op(next3) ex(next4)������һ��ҲΪ'('����еݹ鵽��һ��
            (left1,next3)=parseExp(index+1)#��'('��һ��λ�ã��ݹ飬next3��ֵ��parseExp(index+1)���һ�εݹ�ķ���ֵ��һ
            (right1,next4)=parseExp(next3+1)
            if tokens[next3]== '+':
                return (Sum(left1,right1),next4+1)
            if tokens[next3] == '-':
                return (Diff(left1,right1),next4+1)
            if tokens[next3] == '*':
                return (Prod(left1,right1),next4+1)    
            if tokens[next3] == '/':
                return (Quot(left1,right1),next4+1)
            if tokens[next3] == '=':
                return (Assign(left1,right1),next4+1)
    (parsedExp,nextIndex) = parseExp(0)
    return parsedExp
# returns True if contains only digits
def numberTok(token):
    for char in token:
        if not char in string.digits: return False
    return True

# token is a string
# returns True its first character is a letter
def variableTok(token):
    for char in token:
        if char in string.letters: return True
    return False

# thing is any Python entity
# returns True if it is a number
def isNum(thing):
    return type(thing) == int or type(thing) == float

# Run calculator interactively
def calc():
    env = {}
    while True:
        e = raw_input('%')
        c=parse(tokenize(e))# prints %, returns user input
        print '%', c.eval(env)# your expression here
        print '   env =', env
#calc()
# exprs is a list of strings
# runs calculator on those strings, in sequence, using the same environment
def calcTest(exprs):
    env = {}
    for e in exprs:
        print '%', e  # e is the experession 
        print parse(tokenize(e)).eval(env)# your expression here
        print '   env =', env
        
'''
Answers are:
['fred']
['777']
['777', 'hi', '33']
['*', '*', '-', ')', '(']
['(', 'hi', '*', 'ho', ')']
['(', 'fred', '+', 'george', ')']
['(', 'hi', '*', 'ho', ')']
['(', 'fred', '+', 'george', ')']
'''
def testTokenize():
    print tokenize('fred')
    print tokenize('777 ')
    print tokenize('777 hi 33 ')
    print tokenize('**-)(')
    print tokenize('( hi * ho )')
    print tokenize('(fred + george)')
    print tokenize('(hi*ho)')
    print tokenize('( fred+george )')


# Simple parsing tests from the handout
'''Answers are:
Var(a)
Num(888.0)
Sum(Var(fred), Var(george))
Quot(Prod(Var(a), Var(b)), Diff(Var(cee), Var(doh)))
Quot(Prod(Var(a), Var(b)), Diff(Var(cee), Var(doh)))
Assign(Var(a), Prod(Num(3.0), Num(5.0)))
'''
def testParse():
    print parse(['a'])
    print parse(['888'])
    print parse(['(', 'fred', '+', 'george', ')'])
    print parse(['(', '(', 'a', '*', 'b', ')', '/', '(', 'cee', '-', 'doh', ')' ,')'])
    print parse(tokenize('((a * b) / (cee - doh))'))
    print parse(tokenize('(a = (3 * 5))'))

####################################################################
# Test cases for EAGER evaluator
####################################################################

def testEval():
    env = {}
    Assign(Variable('a'), Number(5.0)).eval(env)
    print Variable('a').eval(env)
    env['b'] = 2.0
    print Variable('b').eval(env)
    env['c'] = 4.0
    print Variable('c').eval(env)
    print Sum(Variable('a'), Variable('b')).eval(env)
    print Sum(Diff(Variable('a'), Variable('c')), Variable('b')).eval(env)
    Assign(Variable('a'), Sum(Variable('a'), Variable('b'))).eval(env)
    print Variable('a').eval(env)
    print env

# Basic calculator test cases (see handout)
testExprs = ['(2 + 5)',
             '(z = 6)',
             'z',
             '(w = (z + 1))',
             'w'
             ]
#calcTest(testExprs)

class Tokenizer(SM):#״̬��
    def __init__(self):
        self.startState = ''
    def getNextValues(self, state, inp):
        if inp == ' ':
            return self.startState, self.state
        if (inp.isalpha() and self.state.isalpha()) or (inp.isdigit() and self.state.isdigit()):#������ĸ���ڻ�������������
            self.state=self.state+inp
            return self.state, self.startState
        else:
            return inp, self.state
def tokenize2(inputstring):#ȥ��''
    list2=Tokenizer().transduce(inputstring)
    while '' in list2:
        list2.remove('')
    return list2
   
####################################################################
# Test cases for LAZY evaluator
####################################################################

# Simple lazy eval test cases from handout
'''Answers are:
Sum(Var(b), Var(c))
Sum(2.0, Var(c))
6.0
'''
def testLazyEval():
    env = {}
    Assign(Variable('a'), Sum(Variable('b'), Variable('c'))).eval(env)
    print Variable('a').eval(env)
    env['b'] = Number(2.0)
    print Variable('a').eval(env)
    env['c'] = Number(4.0)
    print Variable('a').eval(env)

# Lazy partial eval test cases (see handout)
lazyTestExprs = ['(a = (b + c))',
                  '(b = ((d * e) / 2))',
                  'a',
                  '(d = 6)',
                  '(e = 5)',
                  'a',
                  '(c = 9)',
                  'a',
                  '(d = 2)',
                  'a']
# calcTest(lazyTestExprs)

## More test cases (see handout)
partialTestExprs = ['(z = (y + w))',
                    'z',
                    '(y = 2)',
                    'z',
                    '(w = 4)',
                    'z',
                    '(w = 100)',
                    'z']

# calcTest(partialTestExprs)
