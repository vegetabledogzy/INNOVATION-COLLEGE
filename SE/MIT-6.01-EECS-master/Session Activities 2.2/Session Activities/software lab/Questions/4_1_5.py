from lib601.sig import Signal,ConstantSignal,Rn


def polyR(Signal, p):
    c = p.coeffs
    a = ConstantSignal(0)
    for i in range(len(c)):
        a = a + c[i] * Rn(Signal, len(c) - i - 1)
    return a