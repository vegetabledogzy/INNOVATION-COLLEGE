# -*- coding: UTF-8 -*-

# class FirstWordSM(sm.SM):
# Test 1
test1 = '''hi
ho'''
# This can also be writtent as:
# test1 = 'hi\nho'

#Test 2
test2 = '''  hi
ho'''
# This can also be writtent as:
# test2 = '  hi\nho'

#Test 3
test3 = '''

 hi
 ho ho ho

 ha ha ha'''
# This can also be writtent as:
# test3 ='\n\n hi \nho ho ho\n\n ha ha ha'


class FirstWordSM(object):
    startState = False
    state = False
    flag = True  # 换行标识符

    def getNextValues(self, state, inp):
        if self.flag:
            if inp == '\n':
                self.flag = True
            if state:
                if inp == '\n':
                    return False, None
                elif inp != ' ':
                    return True, inp
                else:
                    self.flag = False
                    return False, None
            else:
                if inp == '\n':
                    return False, None
                elif inp != ' ':
                    return True, inp
                else:
                    return False, None
        else:
            # 本行已经输出过，不再输出字符了
            if inp == '\n':
                self.flag = True
            return False, None

    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]


def runTestsFW():
    m = FirstWordSM()
    print 'Test1:', m.transduce(test1)
    print 'Test2:', m.transduce(test2)
    print 'Test3:', m.transduce(test3)
    m = FirstWordSM()
    m.start()
    [m.getNextValues(m.state, i) for i in '\nFoo ']
    print 'Test4', [m.step(i) for i in test1]


runTestsFW()

# execute runTestsFW() to carry out the testing, you should get:
# Test1: ['h', 'i', None, 'h', 'o']
# Test2: [None, None, 'h', 'i', None, 'h', 'o']
# Test3: [None, None, None, 'h', 'i', None, None, 'h', 'o', None, None, None, None, None, None, None, None, None, 'h', 'a', None, None, None, None, None, None]
# Test4: ['h', 'i', None, 'h', 'o']