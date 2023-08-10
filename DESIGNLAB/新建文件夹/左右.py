import lib601.sm as sm
#part1
class BA1(sm.SM):
	startState = 0
	def getNextValues(self, state, inp):
		if inp != 0:
			newState = state * 1.02 + inp - 100
		else:
			newState = state * 1.02
		return (newState, newState)

class BA2(sm.SM):
	startState = 0
	def getNextValues(self, state, inp):
		newState = state * 1.01 + inp
		return (newState, newState)
ba1=BA1()
ba2=BA2()
maxAccount = sm.Cascade(sm.Parallel(ba1,ba2),sm.PureFunction(max))

#part2
class condition1(sm.SM):
        def getNextValues(self,state,inp):
                if abs(inp)>3000:
                        return (state,(inp,0))
                else:
                        return (state,(0,inp))

switchAccount = sm.Cascade(condition1(),sm.Cascade(sm.Parallel2(ba1,ba2),sm.PureFunction(sum)))
#²âÊÔÀı£º
test=[1000,5000,-2000,3000]
maxAccount.transduce(test)
switchAccount.transduce(test)
