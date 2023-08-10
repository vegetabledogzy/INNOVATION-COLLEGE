import lib601.poly as poly
import lib601.sig
from lib601.sig import *

## You can evaluate expressions that use any of the classes or
## functions from the sig module (Signals class, etc.).  You do not
## need to prefix them with "sig."


s = StepSignal()
#��λ���庯��
u = UnitSampleSignal()


#��һ��
#��ʽһ
s1 = ScaledSignal(s,3)
r1= Rn(s1,3)
step1 = r1
#��ʽ��
#step1 = Rn(ScaledSignal(s,3),3)
#��ͼ�鿴
#s1.plot(-1,10) 

#�ڶ���
#��ʽһ
s2 = ScaledSignal(s,-3)
r2 = Rn(s2,7)
step2 = r2
#��ʽ��
#step2 = Rn(ScaledSignal(s,-3),7)
#��ͼ���
#step2.plot(-3,10)

#������
stepUpDown = SummedSignal(step1,R(step2))
#��ͼ���
stepUpDown.plot(0,10)


#������
stepUpDownPoly = polyR(u,poly.Polynomial([5,0,3,0,1,0]))
#��ͼ���
#stepUpDownPoly.plot(0,10)


#��ӡ���ĺ���
def samplesInRange(signal,lo,hi):
    return [signal.sample(i) for i in range(lo,hi)]
#print samplesInRange(step2,0,10)

