# -*- coding:utf-8 -*-
import lib601.sig as sig
import lib601.ts as ts
import lib601.poly as poly
import lib601.sf as sf

desiredRight = 0.5


def controller(k):
    return sf.Gain(k)


def plant1(T):
    return sf.Cascade(sf.R(), sf.Gain(T))


def plant2(T, V):
    # 我感觉两种写法都可以 但前者貌似在流程图中不好表示
    # return sf.Cascade(sf.Cascade(V, sf.R()) * T, sf.FeedbackAdd(sf.Gain(1), sf.R()))
    return sf.Cascade(sf.Cascade(sf.Gain(V*T), sf.R()), sf.FeedbackAdd(sf.Gain(1), sf.R()))


def wallFollowerModel(k, T, V):
    return sf.FeedbackSubtract(sf.Cascade(controller(k), sf.Cascade(plant1(T), plant2(T, V))))


def plotD(k, end=50):
  d = ts.TransducedSignal(sig.ConstantSignal(0.7),
                          wallFollowerModel(k, 0.1, 0.1))
  d.plot(0, end, newWindow='Gain '+str(k))
