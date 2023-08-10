import lib601.sf as sf
import lib601.poly as poly
import lib601.sig as sig
import lib601.ts as ts

s1 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([-1, -5.0/6, 1]))
print 's1.differenceEquation', s1.differenceEquation()
print 's1.dominantPole():', s1.dominantPole()

# 1.5
# stable no
# oscillatory  yes

s2 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([3.0/8, 5.0/4, 1]))
print 's2.differenceEquation', s2.differenceEquation()
print 's2.dominantPole():', s2.dominantPole()
# -2.0
# stable no
# oscillatory  yes

s3 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([9.0/8, 3.0/2, 1]))
print 's3.differenceEquation', s3.differenceEquation()
print 's3.dominantPole():', s3.dominantPole()

# (-0.666666666667+0.666666666667j)
# stable yes
# oscillatory  no

s4 = sf.SystemFunction(poly.Polynomial([1]), poly.Polynomial([1.0/2, 1, 1]))
print 's4.differenceEquation', s4.differenceEquation()
print 's4.dominantPole():', s4.dominantPole()

# (-1+1j)
# stable no
# oscillatory  yes


def plotOutput(d, c):
    """Plot the output of the given SF, with a unit-step signal as input"""
    smModel = sf.DifferenceEquation(d, c).stateMachine()
    outSig = ts.TransducedSignal(sig.UnitSampleSignal(), smModel)
    outSig.plot(0, 200)

# s5
plotOutput([1], [13.0/8, -42.0/64])

