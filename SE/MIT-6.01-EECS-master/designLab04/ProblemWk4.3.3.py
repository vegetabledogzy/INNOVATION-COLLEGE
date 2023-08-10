# Use sm.R, sm.Gain, sm.Cascade, sm.FeedbackAdd and sm.FeedbackSubtract
# to construct the state machines
import lib601.sm as sm

# the output before the first input, init
def accumulator(init):
    return sm.Cascade(init, sm.Cascade(init, sm.R(init)))


# the output at time 0, init
def accumulatorDelay(init):
    return sm.Cascade(init, sm.R(init))
	

# the scale factor s  the output at time 0, init
def accumulatorDelayScaled(s, init):
	return sm.Cascade(init, sm.R(sm.Gain(s)))

