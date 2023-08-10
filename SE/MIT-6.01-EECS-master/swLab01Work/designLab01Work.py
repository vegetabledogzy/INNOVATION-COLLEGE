# -*- coding: UTF-8 -*-
import math
import numpy as np


class Polynomial(object):
    def __init__(self, coefficients):
        self.coefficients = coefficients
        # self.coefficients = map(str, coefficients)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __call__(self, x):
        return self.val(x)

    def __repr__(self):
        return str(self)

    def __str__(self):
        string = ""
        temp5 = ['z**4', 'z**3', 'z**2', 'z', '']
        temp4 = ['z**3', 'z**2', 'z', '']
        temp3 = ['z**2', 'z', '']
        temp2 = ['z', '']
        temp1 = ['']
        temp_dict = {1: temp1, 2: temp2, 3: temp3, 4: temp4, 5: temp5}
        temp = temp_dict[len(self.coefficients)]
        for i, item in enumerate(self.coefficients):
            string = string + str(round(item, 3)) + temp[i] + ' + '
        string = string[:-3]
        return string

    def add(self, other):
        # 前面补0 使得两个数组的长度相同  用numpy进行加法运算
        if len(self.coefficients) > len(other.coefficients):
            for i in range(len(self.coefficients) - len(other.coefficients)):
                other.coefficients.insert(0, 0)
        else:
            for i in range(len(other.coefficients) - len(self.coefficients)):
                self.coefficients.insert(0, 0)

        result = np.array(other.coefficients) + np.array(self.coefficients)
        for item in self.coefficients:
            if item:
                break
            else:
                self.coefficients.remove(item)
        for item in other.coefficients:
            if item:
                break
            else:
                other.coefficients.remove(item)
        return Polynomial(list(result))

    def mul(self, other):
        # 去除数组开头的 0
        for item in self.coefficients:
            if item:
                break
            else:
                self.coefficients.remove(item)
        for item in other.coefficients:
            if item:
                break
            else:
                other.coefficients.remove(item)
        result = [0 for i in range(len(self.coefficients) + len(other.coefficients) - 1)]
        for i in range(len(other.coefficients)):
            for j in range(len(self.coefficients)):
                result[-1 - j - i] = result[-1 - j - i] + other.coefficients[-1 - i] * self.coefficients[-1 - j]
        return Polynomial(result)

    def val(self, x):
        return float(x * x * self.coefficients[0] + x * self.coefficients[1] + self.coefficients[2])

    def coeff(self, i):
        pass

    def roots(self):
        a = 0
        b = 0
        c = 0
        if len(self.coefficients) > 3:
            # raise Exception('Order too high to solve for roots.')
            # print('self.coefficients', self.coefficients)
            return 'Order too high to solve for roots.'
        try:
            c = self.coefficients[-1]
            b = self.coefficients[-2]
            a = self.coefficients[-3]
        except Exception as e:
            pass
        finally:
            if a == 0:
                return -int(c) / b
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
                raise TypeError('Bad operand type')
            delta = math.pow(b, 2) - 4 * a * c
            # 如果是复数的话
            if delta < 0:
                delta = -delta
                x1 = (math.sqrt(delta)*1j - b) / (2 * a)
                x2 = -(math.sqrt(delta)*1j + b) / (2 * a)
                return [x1, x2]
            else:
                x1 = (math.sqrt(delta) - b) / (2 * a)
                x2 = -(math.sqrt(delta) + b) / (2 * a)
                return [x1, x2]


p1 = Polynomial([1, 2, 3])
print p1
p2 = Polynomial([100, 200])
print p1.add(p2)
print p1 + p2
print p1(1)
print p1(-1)
print (p1 + p2)(10)
print p1.mul(p1)
print p1 * p1
print p1 * p2 + p1
print p1.roots()
print p2.roots()
p3 = Polynomial([3, 2, -1])
print p3.roots()
print(p1 * p1).roots()
