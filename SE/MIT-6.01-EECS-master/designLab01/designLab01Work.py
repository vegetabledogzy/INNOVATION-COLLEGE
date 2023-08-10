# -*- coding: UTF-8 -*-
import math


class CalcEquation(object):
    @staticmethod
    def calc(input_string):

        num = input_string.split(' ')
        a = float(num[0])
        b = float(num[1])
        c = float(num[2])
        if a == 0:
            if b != 0:
                return -(c / b)
            else:
                return TypeError("Error!")
        delta = math.pow(b, 2) - 4 * a * c
        if delta < 0:
            return 'No roots'
        x1 = (math.sqrt(delta) - b) / (2 * a)
        x2 = -(math.sqrt(delta) + b) / (2 * a)
        return x1, x2


user = CalcEquation
print "Please enter only numbers separated by spaces:"
string = raw_input()
result = user.calc(string)
print(result)
