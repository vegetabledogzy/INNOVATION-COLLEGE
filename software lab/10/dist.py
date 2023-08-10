# uncompyle6 version 3.8.0
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: c:\Users\robot\Desktop\newversion\codesandbox\lib601\dist.py
# Compiled at: 2011-01-02 23:08:58
"""
Discrete probability distributions
"""
import random, operator, copy, util

class DDist:
    """
    Discrete distribution represented as a dictionary.  Can be
    sparse, in the sense that elements that are not explicitly
    contained in the dictionary are assumed to have zero probability.
    """

    def __init__(self, dictionary):
        self.d = dictionary

    def dictCopy(self):
        """
        @returns: A copy of the dictionary for this distribution.
        """
        return self.d.copy()

    def prob(self, elt):
        """
        @param elt: an element of the domain of this distribution
        (does not need to be explicitly represented in the dictionary;
        in fact, for any element not in the dictionary, we return
        probability 0 without error.)
        @returns: the probability associated with C{elt}
        """
        if self.d.has_key(elt):
            return self.d[elt]
        else:
            return 0

    def support(self):
        """
        @returns: A list (in arbitrary order) of the elements of this
        distribution with non-zero probabability.
        """
        return [ k for k in self.d.keys() if self.prob(k) > 0 ]

    def __repr__(self):
        if len(self.d.items()) == 0:
            return 'Empty DDist'
        else:
            dictRepr = reduce(operator.add, [ util.prettyString(k) + ': ' + util.prettyString(p) + ', ' for (k, p) in self.d.items()
                                            ])
            return 'DDist(' + dictRepr[:-2] + ')'

    __str__ = __repr__

    def draw(self):
        """
        @returns: a randomly drawn element from the distribution
        """
        r = random.random()
        sum = 0.0
        for val in self.support():
            sum += self.prob(val)
            if r < sum:
                return val

    def maxProbElt(self):
        """
        @returns: The element in this domain with maximum probability
        """
        return util.argmax(self.support(), self.prob)

    def marginalizeOut(self, index):
        """
        @param index: index of a random variable to sum out of the
        distribution
        @returns: DDist on all the rest of the variables
        """
        result = {}
        for e in self.support():
            incrDictEntry(result, removeElt(e, index), self.prob(e))

        return DDist(result)

    def conditionOnVar(self, index, value):
        """
        @param index: index of a variable in the joint distribution
        @param value: value of that variable

        @returns: new distribution, conditioned on variable C{i}
        having value C{value}, and with variable C{i} removed from all
        of the elements (it's redundant at this point).
        """
        newElements = [ e for e in self.support() if e[index] == value ]
        z = sum([ self.prob(e) for e in newElements ])
        return DDist(dict([ (removeElt(e, index), self.prob(e) / z) for e in newElements
                          ]))


def JDist(PA, PBgA):
    """
    Create a joint distribution on P(A, B) (in that order),
    represented as a C{DDist}
        
    @param PA: a C{DDist} on some random var A
    @param PBgA: a conditional probability distribution specifying
    P(B | A) (that is, a function from elements of A to C{DDist}
    on B)
    """
    d = {}
    for a in PA.support():
        for b in PBgA(a).support():
            d[(a, b)] = PA.prob(a) * PBgA(a).prob(b)

    return DDist(d)


def bayesEvidence(PA, PBgA, b):
    """
    @param PBgA: conditional distribution over B given A (function
    from values of a to C{DDist} over B)
    @param PA: prior on A
    @param b: evidence value for B = b 
    @returns: P(A | b)
    """
    return JDist(PA, PBgA).conditionOnVar(1, b)


def totalProbability(PA, PBgA):
    """
    @param PBgA: conditional distribution over B given A (function
    from values of a to C{DDist} over B)
    @param PA: distribution over A (object of type C{DiscreteDist})
    @returns: P(B) using the law of total probability.
    C{self} represents P(B | A);  P(A) is the argument to the
    method; we compute and return P(B) as sum_a P(B | a) P(a)
    """
    return JDist(PA, PBgA).marginalizeOut(0)


def DeltaDist(v):
    """
    Distribution with all of its probability mass on value C{v}
    """
    return DDist({v: 1.0})


def UniformDist(elts):
    """
    Uniform distribution over a given finite set of C{elts}
    @param elts: list of any kind of item
    """
    p = 1.0 / len(elts)
    return DDist(dict([ (e, p) for e in elts ]))


class MixtureDist:
    """
    A mixture of two probabability distributions, d1 and d2, with
    mixture parameter p.  Probability of an
    element x under this distribution is p * d1(x) + (1 - p) * d2(x).
    It is as if we first flip a probability-p coin to decide which
    distribution to draw from, and then choose from the approriate
    distribution.

    This implementation is lazy;  it stores the component
    distributions.  Alternatively, we could assume that d1 and d2 are
    DDists and compute a new DDist.
    """

    def __init__(self, d1, d2, p):
        self.d1 = d1
        self.d2 = d2
        self.p = p
        self.binom = DDist({True: p, False: 1 - p})

    def prob(self, elt):
        return self.p * self.d1.prob(elt) + (1 - self.p) * self.d2.prob(elt)

    def draw(self):
        if self.binom.draw():
            return self.d1.draw()
        else:
            return self.d2.draw()

    def support(self):
        return list(set(self.d1.support()).union(set(self.d2.support())))

    def __str__(self):
        result = 'MixtureDist({'
        elts = self.support()
        for x in elts[:-1]:
            result += str(x) + ' : ' + str(self.prob(x)) + ', '

        result += str(elts[(-1)]) + ' : ' + str(self.prob(elts[(-1)])) + '})'
        return result

    __repr__ = __str__


def triangleDist(peak, halfWidth, lo=None, hi=None):
    """
    Construct and return a DDist over integers. The
    distribution will have its peak at index C{peak} and fall off
    linearly from there, reaching 0 at an index C{halfWidth} on
    either side of C{peak}.  Any probability mass that would be below
    C{lo} or above C{hi} is assigned to C{lo} or C{hi}
    """
    d = {}
    d[util.clip(peak, lo, hi)] = 1
    total = 1
    fhw = float(halfWidth)
    for offset in range(1, halfWidth):
        p = (halfWidth - offset) / fhw
        incrDictEntry(d, util.clip(peak + offset, lo, hi), p)
        incrDictEntry(d, util.clip(peak - offset, lo, hi), p)
        total += 2 * p

    for (elt, value) in d.items():
        d[elt] = value / total

    return DDist(d)


def squareDist(lo, hi, loLimit=None, hiLimit=None):
    """
    Construct and return a DDist over integers.  The
    distribution will have a uniform distribution on integers from
    lo to hi-1 (inclusive).
    Any probability mass that would be below
    C{lo} or above C{hi} is assigned to C{lo} or C{hi}.
    """
    d = {}
    p = 1.0 / (hi - lo)
    for i in range(lo, hi):
        incrDictEntry(d, util.clip(i, loLimit, hiLimit), p)

    return DDist(d)


def removeElt(items, i):
    """
    non-destructively remove the element at index i from a list;
    returns a copy;  if the result is a list of length 1, just return
    the element  
    """
    result = items[:i] + items[i + 1:]
    if len(result) == 1:
        return result[0]
    else:
        return result


def incrDictEntry(d, k, v):
    """
    If dictionary C{d} has key C{k}, then increment C{d[k]} by C{v}.
    Else set C{d[k] = v}.
    
    @param d: dictionary
    @param k: legal dictionary key (doesn't have to be in C{d})
    @param v: numeric value
    """
    if d.has_key(k):
        d[k] += v
    else:
        d[k] = v