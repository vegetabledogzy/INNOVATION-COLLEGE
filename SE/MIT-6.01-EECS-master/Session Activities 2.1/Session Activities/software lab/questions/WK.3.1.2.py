import lib601.sm as sm


class Cascade(sm.SM):
	def __init__(self, sm1, sm2):
		self.sm1 = sm1
		self.sm2 = sm2
	
	def getNextValues(self, state, inp):
		(sm1, sm2) = state
		(newSM1, o1) = self.sm1.getNextValues(sm1, inp)
		(newSM2, o2) = self.sm2.getNextValues(sm2, o1)
		return ((newSM1, newSM2), o2)