# -*- coding:utf-8 -*-
import lib601.sm as sm

# Part 1: Sum machine
class Accumulator(sm.SM):
    startState = 0

    def __init__(self, initialValue):
        self.startState = initialValue

    def getNextValues(self, state, inp):
        return state + inp, state + inp


# c = Accumulator(0)
# c.start()
# print c.transduce(list(range(100)))


class SumTSM(sm.SM):

    def __init__(self, initialValue):
        self.startState = initialValue

    def getNextValues(self, state, inp):
        return state + inp, state + inp

    def done(self, state):
        return state > 100


def test1():
    m = SumTSM(0)
    print m.transduce([10, 29, 30, 50, 60])[-1]

test1()

# Part 2: Some machine
fourTime = sm.Repeat(SumTSM(0), 4).transduce(range(0, 1000, 10))
print fourTime


# class SumTSM(sm.SM):
#
#     def __init__(self, initialValue):
#         self.startState = initialValue
#
#     def getNextValues(self, state, inp):
#         return state + inp, state + inp
#
#     def done(self, state):
#         return state
    # def transduce(self, inputs):
    #     self.start()
    #     for inp in inputs:
    #         num_sum = self.step(inp)
    #         if num_sum >=100:
    #             return 'current_num', inp, 'num_sum', num_sum

# fourTimes = sm.Repeat(CharTSM('a'), 4).run()
# print fourTimes


#
# fourTimes = RepeatSumTSM(4).repeat_SumTSM()
# print fourTimes
# Part 3: Counting machine
# class CountUpTo(sm.SM):
#     def __init__(self, init_time):
#         self.init_time = init_time
#
#     def run(self, run_time):
#         if self.init_time >= run_time:
#             return list(range(1, run_time + 1))
#         else:
#             return list(range(1, self.init_time + 1))
#
#
# # m = CountUpTo(3)
# # result = m.run(20)
# # print(result)
#
# # Part 4: Multiple Counting machine
#
#
# def makeSequenceCounter(nums):
#
#     class MyCountUpTo(sm.SM):
#         def __init__(self, nums):
#             self.nums = nums
#
#         def run(self, run_time):
#             result = []
#             for num in self.nums:
#                 for i in CountUpTo(num).run(run_time):
#                     result.append(i)
#             print result
#     return MyCountUpTo(nums)
#
#
# makeSequenceCounter([2, 5, 3]).run(20)

