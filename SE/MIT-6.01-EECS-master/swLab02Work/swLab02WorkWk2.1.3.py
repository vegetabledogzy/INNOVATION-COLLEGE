class Delay2Machine(object):
    def __init__(self, val0, val1):
        self.startState = val0
        self.state = val0
        self.nextState = val1
        pass

    def getNextValues(self, state, inp):
        current_output = state
        return self.nextState, current_output

    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        self.nextState = inp
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]


def runTestsDelay():
    print 'Test1:', Delay2Machine(100, 10).transduce([1, 0, 2, 0, 0, 3, 0, 0, 0, 4])
    print 'Test2:', Delay2Machine(10, 100).transduce([0, 0, 0, 0, 0, 0, 1])
    print 'Test3:', Delay2Machine(-1, 0).transduce([1, 2, -3, 1, 2, -3])
    # Test that self.state is not being changed.
    m = Delay2Machine(100, 10)
    m.start()
    [m.getNextValues(m.state, i) for i in [-1, -2, -3, -4, -5, -6]]
    print 'Test4:', [m.step(i) for i in [1, 0, 2, 0, 0, 3, 0, 0, 0, 4]]


# execute runTestsDelay() to carry out the testing, you should get:
# Test1: [100, 10, 1, 0, 2, 0, 0, 3, 0, 0]
# Test2: [10, 100, 0, 0, 0, 0, 0]
# Test3: [-1, 0, 1, 2, -3, 1]
# Test4: [100, 10, 1, 0, 2, 0, 0, 3, 0, 0]

runTestsDelay()

