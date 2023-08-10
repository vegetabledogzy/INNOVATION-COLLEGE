"""
Class and some supporting functions for representing and manipulating system functions. 
"""

import math
import lib601.poly as poly
import lib601.util as util


class SystemFunction:
    """
    Represent a system function as a ratio of polynomials in R
    """
    def __init__(self, numeratorPoly, denominatorPoly):
        self.numerator = numeratorPoly
        self.denominator = denominatorPoly

    def __str__(self):
        return 'SF(' + self.numerator.__str__('R') + \
               '/' + self.denominator.__str__('R') + ')'

    __repr__ = __str__

    def poles(self):
        return poly.Polynomial(self.denominator.coeffs[::-1]).roots()

    def poleMagnitudes(self):
        """
        returns a list of the magnitudes of the poles of the system. The magnitude of a real pole is simply its absolute value.
        The magnitude of a complex pole is the square root of the sum of the squares of its real and imaginary parts.
        The abs function in Python does the appropriate computation for both types.
        :return:
        """
        a = []
        for i in range(len(self.poles())):
            a.append(abs(self.poles()[i]))
        return a

    def dominantPole(self):
        """
        returns one of the poles with greatest magnitude.
         If two or more poles have the same greatest magnitude,
        then any of these poles may be returned. Detailed
        """
        return max(self.poles())


# 1. -2 1 / -1 1
# 2.  1 0 1 / -1 1
# 3.  -2 1 -2 1 / 1 -2 1

# n_1 * d_2
# d_1*d_2 + n_1*n_2

def Cascade(sf1, sf2):
    s = SystemFunction(None, None)
    s.numerator = sf1.numerator * sf2.numerator
    s.denominator = sf1.denominator + sf2.denominator
    return s


def FeedbackSubtract(sf1, sf2=None):
    s = SystemFunction(None, None)
    s.numerator = sf1.numerator * sf2.denominator + sf2.numerator+sf1.denominator
    s.denominator = sf1.denominator * sf2.denominator
    return s

