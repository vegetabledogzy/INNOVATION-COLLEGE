# coding=utf-8
# str = '''def f(x): # comment
# return 1'''
# print(len(str))
# print(i for i in str)
x1 = '''def f(x):  # func
   if x:   # test
     # comment
     return 'foo' '''

x2 = '''#initial comment
def f(x):  # func
   if x:   # test
     # comment
     return 'foo' '''

 
class CommentsSM(object):

    startState = False
    state = False

    def getNextValues(self, state, inp):
        if not state:
            if inp == '#':
                return True, inp
            else:
                return False, None
        else:
            if inp == '\n':
                return False, None
            else:
                return True, inp


    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]


def runTestsComm():
    m = CommentsSM()
    # Return only the outputs that are not None
    print 'Test1:', [c for c in CommentsSM().transduce(x1) if not c == None]
    print 'Test2:', [c for c in CommentsSM().transduce(x2) if not c == None]
    # Test that self.state is not being changed.
    m = CommentsSM()
    m.start()
    [m.getNextValues(m.state, i) for i in ' #foo #bar']
    print 'Test3:', [c for c in [m.step(i) for i in x2] if not c == None]


runTestsComm()
# execute runTestsComm() to carry out the testing, you should get:

# Test1: ['#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
# Test2: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
# Test3: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
