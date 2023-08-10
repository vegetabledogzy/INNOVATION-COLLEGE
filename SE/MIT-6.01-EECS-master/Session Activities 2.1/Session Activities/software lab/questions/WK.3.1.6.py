# -*- coding:utf-8 -*-
import lib601.sm as sm

negate = sm.PureFunction(lambda x: True if x==False else False)
print negate
alternating = sm.Feedback(sm.Cascade(negate, sm.Delay(True))).run(verbose=True)
print alternating
